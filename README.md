# Bockchain-Based-voting-platform
Blockchain is a technology that is rapidly gaining momentum in the era of industry 4.0. With high security and transparency provisions, it is being widely used in supply chain management systems, healthcare, payments, business, IoT, voting systems, etc.
<H2>Why do we need it?</H2>
Current voting systems like ballot box voting or electronic voting suffer from various security threats such as DDoS attacks, polling booth capturing, vote alteration and manipulation, malware attacks, etc, and also require huge amounts of paperwork, human resources, and time. This creates a sense of distrust among existing systems.<br><br>
Some of the disadvantages are:
<ul>
  <li>Long Queues during elections</li>
  <li>Security Breaches like data leaks, vote tampering.</li>
  <li>Lot of paperwork involved, hence less eco-friendly and time-consuming.</li>
  <li>Difficult for differently-abled voters to reach polling booth.</li>
  <li>Cost of expenditure on elections is high.</li>
</ul>
<h2>Solution :</h2>
Using blockchain, voting process can be made more secure, transparent, immutable, and reliable. How? Let’s take an example.<br><br>

Suppose you are an eligible voter who goes to polling booth and cast vote using EVM (Electronic Voting Machine). But since it’s a circuitry after all and if someone tampers with microchip, you may never know that did your vote reach to person for whom you voted or was diverted into another candidate’s account?
Since there’s no tracing back of your vote. But, if you use blockchain- it stores everything as a transaction that will be explained soon below; and hence gives you a receipt of your vote (in a form of a transaction ID) and you can use it to ensure that your vote has been counted securely.<br><br>

Now suppose a digital voting system (website/app) has been launched to digitize process and all confidential data is stored on a single admin server/machine, if someone tries to hack it or snoop over it, he/she can change candidate’s vote count- from 2 to 22! You may never know that hacker installs malware or performs clickjacking attacks to steal or negate your vote or simply attacks central server.<br><br>



To avoid this, if system is integrated with blockchain- a special property called immutability protects system. Consider SQL, PHP, or any other traditional database systems. You can insert, update, or delete votes. But in a blockchain you can just insert data but cannot update or delete. Hence when you insert something, it stays there forever and no one can manipulate it- Thus name immutable ledger.<br>

But Building a blockchain system is not enough. It should be decentralized i.e if one server goes down or something happens on a particular node, other nodes can function normally and do not have to wait for victim node’s recovery.<br>

So a gist of advantages are listed below:
<ul><li>You can vote anytime/anywhere (During Pandemics like COVID-19 where it’s impossible to hold elections physically</li><li>Secure</li><li>Immutable</li><li>Faster</li><li>Transparent</li></ul>
<h2>Let’s visualize process</h2>
It is always interesting to learn things if it’s visually explained. Hence diagram given below explains how the blockchain voting works.<br><br>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20200424190016/2020-04-22-21.png">

According to above diagram, voter needs to enter his/her credentials in order to vote. All data is then encrypted and stored as a transaction. This transaction is then broadcasted to every node in network, which in turn is then verified. If network approves transaction, it is stored in a block and added to chain. Note that once a block is added into chain, it stays there forever and can’t be updated. Users can now see results and also trace back transaction if they want.<br>

Since current voting systems don’t suffice to security needs ofmodern generation, there is a need to build a system that leverages security, convenience, and trust involved in voting process. Hence voting systems make use of Blockchain technology to add an extra layer of security and encourage people to vote from any time, anywhere without any hassle and makes voting process more cost-effective and time-saving.<br>








