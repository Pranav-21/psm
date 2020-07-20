#!python
print("content-type:text/html \r\n\r\n")

import cgi

data=cgi.FieldStorage()
rcid=data.getvalue('id')

#print("<h4>{}</h4>".format(rcid))

import pymysql

servername="localhost"
username="root"
password=""
dbname="hardware"

db=pymysql.connect(servername,username,password,dbname)

cur=db.cursor()

query="SELECT * FROM pc WHERE id={}".format(rcid)


cur.execute(query)

row=cur.fetchone()




content='''
       <html>
            <body>
                     <form method="post" action="update.py">
                       <fieldset style="background-color:LightSalmon;"> 
			           <legend style="background-color:Brown;color:white; font-size:40px;" align ="center" ><b>[ Hardware Information ]</b></legend>
                       <table style="width:100%">
                          <tr>
                               <td style="font-size:25px;" align ="right"><strong><big>ID:</big></strong></td>
                                <td><input type="text" name="id" style="width:50%; font-size:25px;" value="{}" readonly></td>
                          </tr>
                          
                          <tr>
					      <td style="font-size:20px;" align ="right"><strong><big>service engineer name:</big></strong></td>
						  <td><input type="text" name="sen" style="width:50%; font-size:20px;" value="{}" required></td>
						  </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
                          <tr>
					      <td style="font-size:25px;" align ="right"><strong><big>department id:</big></strong></td>
						  <td><input type="text" name="did" style="width:50%; font-size:25px;" value="{}" required></td>
						  </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 
					 <tr>
					      <td style="font-size:25px;" align ="right"><strong><big>brand name:</big></strong></td>
						  <td><input type="text" name="bname" style="width:50%; font-size:25px;" value="{}" ></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
				     <tr>
					      <td style="font-size:25px;" align ="right"><strong><big>install date:</big></strong></td>
						  <td><input type="date" name="idate" value="{}" required></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 
					  <tr>
					      <td style="font-size:25px;" align ="right"><strong><big>worrenty:</big></strong></td>
						  <td><input type="text"  name="wor" style="width:50%; font-size:25px;" value="{}" ></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>

				     <tr>
					      <td style="font-size:25px;" align ="right"><strong><big>cpu-processor:</big></strong></td>
						  <td><input type="text" name="pro" style="width:50%; font-size:25px;" value="{}" required></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 
					 <tr>
					      <td style="font-size:25px;" align ="right"><strong><big>cpu-ram:</big></strong></td>
						  <td><input type="text" name="ram" style="width:50%; font-size:25px;" value="{}" required></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 
					 <tr>
					      <td style="font-size:25px;" align ="right"><strong><big>cpu-storage:</big></strong></td>
						  <td><input type="text" name="sto" style="width:50%; font-size:25px;" value="{}" required></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 
					 <tr>
					      <td style="font-size:25px;" align ="right"><strong><big>monitor:</big></strong></td>
						  <td><input type="text" name="mon" style="width:50%; font-size:25px;" value="{}" required></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					      <td style="font-size:25px;" align ="right"><strong><big>printer:</big></strong></td>
						  <td><input type="text" name="pri" style="width:50%; font-size:25px;" value="{}" ></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>


				     <tr>
					      <td style="font-size:25px;" align ="right"><strong><big>lan connection:</big></strong></td>
						  <td ><input type="text" name="lan" style="width:50%; font-size:25px;" value="{}" required></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>

					 <tr>
					      <td style="font-size:25px;" align ="right"><strong><big>repair(if):</big></strong></td>
						  <td><input type="text" name="rep" style="width:50%; font-size:25px;" value="{}" required></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
					 <tr>
					 <td></td>
					 </tr>
                       
                           <tr>
                                   
                              <td colspan="2" style="font-size:30px;" align ="center"><strong><big><input type="submit" name="update" style="background-color:green; color:white; font-size:20px;" value="UPDATE"></big></strong></td>
					 </tr>
                           </tr>
                           
                           <tr>
					          <td style="font-size:25px;"><a href='http://localhost/cgi-bin/display.py'>Database display</a></td>
					       </tr>

                       </table>
                     
                     
                     </form>
            </body>
       
       </html>



'''.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])


print(content)


