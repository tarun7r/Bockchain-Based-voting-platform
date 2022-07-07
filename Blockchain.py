import hashlib
import json
import os
import re
from collections import Counter

import requests
from flask import (Flask, abort, jsonify, make_response, redirect,
                   render_template, request, session, url_for)
from web3 import Web3

app = Flask(__name__, template_folder='template',static_folder='template/assets')



rpc = "https://naklecha.blockchain.azure.com:3200/xxxxxxxxxxxxxxxxxxxxxxxxx"

web3 = Web3(Web3.HTTPProvider(rpc))
abi = '[{"constant":true,"inputs":[],"name":"candidatesCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function","signature":"0x2d35a8a2"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"candidates","outputs":[{"name":"id","type":"uint256"},{"name":"name","type":"string"},{"name":"voteCount","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function","signature":"0x3477ee2e"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"voters","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function","signature":"0xa3ec138d"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor","signature":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_candidateId","type":"uint256"}],"name":"votedEvent","type":"event","signature":"0xfff3c900d938d21d0990d786e819f29b8d05c1ef587b462b939609625b684b16"},{"constant":false,"inputs":[],"name":"end","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function","signature":"0xefbe1c1c"},{"constant":false,"inputs":[{"name":"_candidateId","type":"uint256"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function","signature":"0x0121b93f"}]'
contract_addr = "0x0000000000000000000000000000000000000001"


app = Flask(__name__)
app.secret_key = 'super secret key'

accounts = [  ]

privatekeys = [ ]

vote_tx = []
voted = []
ended = 0



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
      return render_template(r"admin.html", name = name)
     


@app.route('/result',methods = ['POST', 'GET'])
def result():
   render_template(r'admin.html')
   

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

      
      voter_id = vote_hash


     
      if vote[0][0]=='a':
         vote = "Cristano Ronaldo"
      elif vote[0][0]=='b':
         vote  = "Neymar"
      elif vote[0][0] =='c':
         vote = "Lionel Messi"
      
      return render_template(r"check.html",vote = vote, variable = vote_hash)


if __name__ == '__main__':
   app.run(debug = True)
