import hashlib
import os
from collections import Counter

import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template',static_folder='template/assets')




class unique_vote_id:
   
   def __init__(self, previous_block_hash,uniq):
        self.previous_block_hash = previous_block_hash
        self.uniq = uniq
        self.block_data = "-".join(uniq)+"-"+ previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()



@app.route('/vote',methods = ['POST', 'GET'])
def vote():
   render_template(r'sign_in.html')
   if request.method == 'POST':
      result = request.form
      global name
      name = result['name']
      unique_number = result['Aadhar Number']
      initial_block = unique_vote_id("0",unique_number)
      global vote_id
      vote_id = initial_block.block_hash
      
      return render_template(r"vote.html",variable= vote_id, name = name)


@app.route('/admin',methods = ['POST', 'GET'])
def admin():
   render_template(r'admin_signin.html')
   if request.method == 'POST':
      result = request.form
      name = result['name']
      password = result['password']
      if name == "root" and password =="root":
         return render_template(r"admin.html", name = name)
      else:
         pass



@app.route('/result',methods = ['POST', 'GET'])
def result():
   render_template(r'admin.html')
   mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password="root",
                                    database="elections" )
   mycursor = mydb.cursor()
   mycursor.execute("SELECT vote FROM poll")
   
   myresult = mycursor.fetchall()
   result = []
   for x in myresult:
      result.append(x)
   
   duplicate_dict = Counter(result)
   candidate1 = duplicate_dict['a',]
   candidate2 = duplicate_dict['b',]
   candidate3 = duplicate_dict['c',]
   total = int(candidate1)+int(candidate2)+int(candidate3)
   return render_template(r"results.html", c1 = candidate1 , c2= candidate2 , c3 = candidate3,total = total)


@app.route('/thank',methods = ['POST', 'GET'])
def thank():
   render_template(r'vote.html')
   if request.method == 'POST':
      result = request.form
      choice =  result['poll']
      mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="elections" )
      mycursor = mydb.cursor()
      sql = "INSERT INTO poll (voter_id , vote) VALUES (%s, %s)"
      val = (vote_id,choice)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template(r"thank.html",variable= vote_id, name=name)


@app.route('/check_signin')
def check_signin():
   render_template(r'thank.html')
   return render_template(r"check_signin.html")
    




@app.route('/check',methods = ['POST', 'GET'])
def check():
   render_template(r'check_signin.html')
   if request.method == 'POST':
      result = request.form
      vote_hash = result['name']

      mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="elections" )
      
      mycursor = mydb.cursor()
      voter_id = vote_hash


      sql = """SELECT vote FROM poll WHERE voter_id = '%s'""" % (voter_id)
      mycursor.execute(sql)
      vote = mycursor.fetchall()
      if vote[0][0]=='a':
         vote = "Cristano Ronaldo"
      elif vote[0][0]=='b':
         vote  = "Neymar"
      elif vote[0][0] =='c':
         vote = "Lionel Messi"
      
      return render_template(r"check.html",vote = vote, variable = vote_hash)


if __name__ == '__main__':
   app.run(debug = True)
