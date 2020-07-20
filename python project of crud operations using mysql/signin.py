#!python
print("content-type:text/html \r\n\r\n")

import cgi
import pymysql


data=cgi.FieldStorage()


u=data.getvalue('use')
p=data.getvalue('psw')
p1=data.getvalue('psw1')
#print("<h3>{}</h3>".format(u))

servername="localhost"
username="root"
password=""
dbname="hardware"

db=pymysql.connect(servername,username,password,dbname)

cur=db.cursor()

query="SELECT * FROM sign"

cur.execute(query)

row=cur.fetchone()

pid = row[0]
user = row[1]
password = row[2]
#print("{}",user)
if (u == user) and (p == password):  
           print("Please click on database dislplay to see the database information")
           print("<a style='font-size:25px;' href='http://localhost/cgi-bin/display.py'>Database display</a>")
           print("Please click on change user and password to change the both")
           print("<a style='font-size:25px;' href='http://localhost/changesign.html'>Change username & password</a>")
								
      
else:
    print("That is the wrong username.")    