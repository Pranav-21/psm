#!python
print("content-type:text/html \r\n\r\n")

print("<h1 align ='center' style='font-size:40px;'><b>Records From <ins>Database</ins></b></h1>")

start='''
       <table style="width:50%" style="font-size:20px;" align ="center" border=1>
        <style>
              body {background-color: LightYellow;}
            h1 {color: red;}
            p {color: blue;}
             </style>
					 
          <tr align ="center" style="background-color:Brown;color:white;font-size:20px;">
             <td align ="center">department id</td>
             <td align ="center">Edit</td>
             <td align ="center">View</td>
             <td align ="center">Delete</td>
             
          </tr>
          
'''

print(start) 

import pymysql

servername="localhost"
username="root"
password=""
dbname="hardware"

db=pymysql.connect(servername,username,password,dbname)

cur=db.cursor()

query="SELECT * FROM pc"

cur.execute(query)

data=cur.fetchall()

for row in data:
    print("<tr align ='center' style='background-color:Bisque;color:Chocolate; font-size:20px;' >")
    
    print("<td>{}</td>".format(row[2]))
    
    print("<td><a href='edit.py?id={}'>Edit</a></td>".format(row[0]))
    
    print("<td><a href='view.py?id={}'>View</a></td>".format(row[0]))
    
    print("<td><a href='delete.py?id={}'>Delete</a></td>".format(row[0]))
    
    print("</tr>")
    
end='''
</table>
    <tr>
            <td ><a style="font-size:25px;" href='http://localhost/pcform.html'>Hardware Entry Form</a></td>
    </tr>
'''

print(end)