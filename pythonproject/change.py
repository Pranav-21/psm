#!python
print("content-type:text/html \r\n\r\n")

import cgi
import pymysql


data=cgi.FieldStorage()


u=data.getvalue('use')
p=data.getvalue('psw')
p1=data.getvalue('psw1')
print("<h3>{}</h3>".format(u))

servername="localhost"
username="root"
password=""
dbname="hardware"

db=pymysql.connect(servername,username,password,dbname)

cur=db.cursor()


query="UPDATE sign SET user='{}',password='{}' WHERE pid=1".format(u,p)

if (p == p1):  
           cur.execute(query)
           db.commit()
           print("successfully updated")
           print("Please click on database dislplay to see the database information")
           print("<a style='font-size:25px;' href='http://localhost/cgi-bin/display.py'>Database display</a>")
           print("Please click for login")
           print("<a style='font-size:25px;' href='http://localhost/sign.html'>Change username & password</a>")
								
      
else:
    print("That is the wrong username.")  
    db.rollback()    