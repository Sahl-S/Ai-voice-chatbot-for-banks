

import mysql.connector
mysqldb=mysql.connector.connect(
 host="localhost"
 ,user="root"
 ,password="root"
 ,port='3306'
 ,database="bank"
)

mycursor=mysqldb.cursor()
'''
mycursor.execute('SELECT * FROM useracc')
mysqldata=mycursor.fetchall()

for user in mysqldata:
 print(user)
'''

def checkfacedb():
 with open('dbname.txt', "r") as dbname:
  facename = dbname.readlines()
  facename=facename[0]
  print(facename)
  mycursor = mysqldb.cursor()
  mycursor.execute(f"SELECT userid FROM userpass WHERE imgpass LIKE '{facename}'")
  mysqldata = mycursor.fetchall()
  useridno=mysqldata[0][0]
  print(useridno)
  return useridno


def dbaccountno():
 global countofaccounts
 #account no
 mycursor = mysqldb.cursor()
 mycursor.execute(f"SELECT accno FROM useracc WHERE userid LIKE '{useridno}'")
 account_no = mycursor.fetchall()
 print(account_no)
 mycursor.execute(f"SELECT COUNT(accno) FROM useracc WHERE userid LIKE '{useridno}'")
 countofaccounts = mycursor.fetchall()
 countofaccounts=countofaccounts[0][0]
 print("No of accounts:",countofaccounts)
 return account_no

def dbcount():
 global countofaccounts
 #account no
 mycursor = mysqldb.cursor()
 mycursor.execute(f"SELECT accno FROM useracc WHERE userid LIKE '{useridno}'")
 account_no = mycursor.fetchall()
 print(account_no)
 mycursor.execute(f"SELECT COUNT(accno) FROM useracc WHERE userid LIKE '{useridno}'")
 countofaccounts = mycursor.fetchall()
 countofaccounts=countofaccounts[0][0]
 print("No of accounts:",countofaccounts)
 return countofaccounts


def dbaccountbalance():
 #balance,account type
 mycursor = mysqldb.cursor()
 mycursor.execute(f"SELECT accno,acctype,balance FROM useracc WHERE userid LIKE '{useridno}'")
 balance = mycursor.fetchall()
 #balance = balance[1][1]
 print(balance)
 '''
 for i in range(countofaccounts-1):
  for j in range(countofaccounts-1):
 '''
 return balance

def dbaccountno():
 #balance,account type
 mycursor = mysqldb.cursor()
 mycursor.execute(f"SELECT accno,acctype,balance FROM useracc WHERE userid LIKE '{useridno}'")
 accno = mycursor.fetchall()
 accno = accno[1][1]
 print(accno)

def dbfullname():
 #customer_fullname
 mycursor = mysqldb.cursor()
 mycursor.execute(f"SELECT fullname FROM userdata WHERE userid LIKE '{useridno}'")
 customer_fullname = mycursor.fetchall()
 customer_fullname=customer_fullname[0][0]
 print(customer_fullname)
 return customer_fullname

def dbemail():
 #email
 mycursor = mysqldb.cursor()
 mycursor.execute(f"SELECT email FROM userdata WHERE userid LIKE '{useridno}'")
 email = mycursor.fetchall()
 email=email[0][0]
 print(email)
 return email

def phone():
 #phone
 mycursor = mysqldb.cursor()
 mycursor.execute(f"SELECT phone FROM userdata WHERE userid LIKE '{useridno}'")
 phone = mycursor.fetchall()
 phone=int(phone[0][0])
 print(phone)
 return phone



useridno=checkfacedb()











#checkfacedb()

