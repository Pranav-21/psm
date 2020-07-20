#!python
print("content-type:text/html \r\n\r\n")

import cgi
import pymysql

from datetime import datetime

t=(datetime.now())


data=cgi.FieldStorage()

en=data.getvalue('sen')
d=data.getvalue('did')
b=data.getvalue('bname')
i=data.getvalue('idate')
w=data.getvalue('wor')
c=data.getvalue('pro')
r=data.getvalue('ram')
s=data.getvalue('sto')
m=data.getvalue('mon')
p=data.getvalue('pri')
l=data.getvalue('lan')
re=data.getvalue('rep')

#print("<h2>{}</h2>".format(d))
#print("<h2>{}</h2>".format(i))
#print("<h2>{}</h2>".format(b))

servername="localhost"
username="root"
password=""
dbname="hardware"

db=pymysql.connect(servername,username,password,dbname)
cur=db.cursor()
query="INSERT INTO pc(service_e_name,departmentid,brandname,installdate,worrenty,processor,ram,storage,monitor,printer,lan,repair)VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(en,d,b,i,w,c,r,s,m,p,l,re)

try:
  
   cur.execute(query)
   db.commit()
   print("<a style='font-size:25px;' href='http://localhost/cgi-bin/display.py'>Database display</a>")
   
except:
   print("error")
   db.rollback()
