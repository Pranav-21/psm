#!python
print("content-type:text/html \r\n\r\n")
import cgi
import pymysql
data=cgi.FieldStorage()
rcid=data.getvalue('id')

#print("<h4>{}</h4>".format(rcid))



servername="localhost"
username="root"
password=""
dbname="hardware"

db=pymysql.connect(servername,username,password,dbname)

cur=db.cursor()

query="DELETE FROM pc WHERE id={}".format(rcid)
try:
 cur.execute(query)
 
 db.commit()
 print("successfully deleted")
 print("<a style='font-size:25px;' href='http://localhost/cgi-bin/display.py'>Database display</a>")
except:
   print("<h4>Error in Query</h4>")
   db.rollback()