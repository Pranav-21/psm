#!python
print("content-type:text/html \r\n\r\n")

import cgi
import pymysql

data=cgi.FieldStorage()

rcid=data.getvalue('id')
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
print("<h3>{}</h3>".format(rcid))


servername="localhost"
username="root"
password=""
dbname="hardware"

db=pymysql.connect(servername,username,password,dbname)
cur=db.cursor()

query="UPDATE pc SET departmentid='{}',brandname='{}',installdate='{}',worrenty='{}',processor='{}',ram='{}',storage='{}',monitor='{}',printer='{}',lan='{}',repair='{}' WHERE id={}".format(d,b,i,w,c,r,s,m,p,l,re,rcid)

try:
  cur.execute(query)
  db.commit()
  print("successfully updated")
   
  print("<td><a style='font-size:25px;' href='http://localhost/cgi-bin/display.py'>Database display</a></td>")
except:
  db.rollback()
  print("Error in Query")

  