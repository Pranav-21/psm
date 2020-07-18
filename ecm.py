
from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


root = Tk()
root.title("Employee Contact List")
width = 1200
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(1, 1)


#============================VARIABLES===================================#
NAME = StringVar()
GENDER = StringVar()
ADDRESS = StringVar()
CONTACT = StringVar()
EMAIL = StringVar()
QUALIFICATION = StringVar()
SKILLS = StringVar()
DEPARTMENT = StringVar()
WORK = StringVar()

#============================METHODS=====================================#

def Database():
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, name TEXT, gender TEXT, address TEXT, contact TEXT, email TEXT, qualification TEXT, skills TEXT, department TEXT, work TEXT)")
    cursor.execute("SELECT * FROM `member` ORDER BY `department` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SubmitData():
     if  NAME.get() == "" or QUALIFICATION.get() == "" or DEPARTMENT.get() == "" or GENDER.get() == "" or SKILLS.get() == "" or ADDRESS.get() == "" or CONTACT.get() == "" or EMAIL.get() == ""or WORK.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
     else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("employee.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `member` (name,  gender, address, contact,email,qualification, skills, department,work) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(NAME.get()),  str(GENDER.get()), str(ADDRESS.get()),  int(CONTACT.get()), str(EMAIL.get()),str(QUALIFICATION.get()), str(SKILLS.get()),  str(DEPARTMENT.get()), str(WORK.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `department` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        NAME.set("")
        GENDER.set("")
        ADDRESS.set("")
        CONTACT.set("")
        EMAIL.set("")
        QUALIFICATION.set("")
        SKILLS.set("")
        DEPARTMENT.set("")
        WORK.set("")
def UpdateData():
     if  NAME.get() == "" or QUALIFICATION.get() == "" or DEPARTMENT.get() == "" or GENDER.get() == "" or SKILLS.get() == "" or ADDRESS.get() == "" or CONTACT.get() == "" or EMAIL.get() == ""or WORK.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
     else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("employee.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `member` SET `name` = ?, `gender` =?,  `address` = ?, `contact` = ?, `email` = ?, `qualification` = ?, `skills` = ?, `department` = ?, `work` = ?  WHERE `mem_id` = ?", (str(NAME.get()),  str(GENDER.get()), str(ADDRESS.get()), int(CONTACT.get()), str(EMAIL.get()),str(QUALIFICATION.get()), str(SKILLS.get()) , str(DEPARTMENT.get()), str(WORK.get()), int(mem_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `department` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        NAME.set("")
        GENDER.set("")
        ADDRESS.set("")
        CONTACT.set("")
        EMAIL.set("")
        QUALIFICATION.set("")
        SKILLS.set("")
        DEPARTMENT.set("")
        WORK.set("")

def OnSelected(event):
    global mem_id, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    NAME.set("")
    GENDER.set("")
    ADDRESS.set("")
    CONTACT.set("")
    EMAIL.set("")
    QUALIFICATION.set("")
    SKILLS.set("")
    DEPARTMENT.set("")
    WORK.set("")
    NAME.set(selecteditem[1])
    ADDRESS.set(selecteditem[3])
    CONTACT.set(selecteditem[4])
    EMAIL.set(selecteditem[5])
    QUALIFICATION.set(selecteditem[6])
    SKILLS.set(selecteditem[7])
    DEPARTMENT.set(selecteditem[8])
    WORK.set(selecteditem[9])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Employee Contact List")
    width = 600
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()
    
    #===================FRAMES==============================#
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
    
    
    #===================LABELS==============================#
    lbl_title = Label(FormTitle, text="Updating Contacts", font=('arial', 16), bg="yellow",  width = 300)
    lbl_title.pack(fill=X)
    lbl_name = Label(ContactForm, text="Name", font=('arial', 14), bd=5)
    lbl_name.grid(row=0, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=1, sticky=W)
    lbl_address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
    lbl_address.grid(row=2, sticky=W)
    lbl_contact = Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
    lbl_contact.grid(row=3, sticky=W)
    lbl_email = Label(ContactForm, text="email", font=('arial', 14), bd=5)
    lbl_email.grid(row=4, sticky=W)
    lbl_qualification = Label(ContactForm, text="Qualification", font=('arial', 14), bd=5)
    lbl_qualification.grid(row=5, sticky=W)
    lbl_skills = Label(ContactForm, text="SKILLS", font=('arial', 14), bd=5)
    lbl_skills.grid(row=6, sticky=W)
    lbl_department = Label(ContactForm, text="Department", font=('arial', 14), bd=5)
    lbl_department.grid(row=7, sticky=W)
    lbl_work = Label(ContactForm, text="work", font=('arial', 14), bd=5)
    lbl_work.grid(row=8, sticky=W)


    #===================ENTRY===============================#
    name = Entry(ContactForm, textvariable=NAME, font=('arial', 14))
    name.grid(row=0, column=1)
    RadioGroup.grid(row=1, column=1)
    address = Entry(ContactForm, textvariable=ADDRESS,  font=('arial', 14))
    address.grid(row=2, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT,  font=('arial', 14))
    contact.grid(row=3, column=1)
    email = Entry(ContactForm, textvariable=EMAIL, font=('arial', 14))
    email.grid(row=4, column=1)
    qualification = Entry(ContactForm, textvariable=QUALIFICATION, font=('arial', 14))
    qualification.grid(row=5, column=1)
    department = Entry(ContactForm, textvariable=DEPARTMENT, font=('arial', 14))
    department.grid(row=6, column=1)
    skills = Entry(ContactForm, textvariable=SKILLS,  font=('arial', 14))
    skills.grid(row=7, column=1)
    work = Entry(ContactForm, textvariable=WORK, font=('arial', 14))
    work.grid(row=8, column=1)

    #==================BUTTONS==============================#
    btn_updatecon = Button(ContactForm, text="Update", width=50,border = "10",activebackground="orange", command=UpdateData)
    btn_updatecon.grid(row=9, columnspan=2, pady=10)

def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("employee.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `member` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def AddNewWindow():
    global NewWindow
    NAME.set("")
    GENDER.set("")
    ADDRESS.set("")
    CONTACT.set("")
    EMAIL.set("")
    QUALIFICATION.set("")
    SKILLS.set("")
    DEPARTMENT.set("")
    WORK.set("")
    NewWindow = Toplevel()
    NewWindow.title("Employee Contact List")
    width = 600
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
    
    #===================FRAMES==============================#
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
    
     #===================LABELS==============================#
    lbl_title = Label(FormTitle, text="Add New Employee Contact", font=('arial', 16), bg="#66ff66",  width = 300)
    lbl_title.pack(fill=X)
    lbl_name = Label(ContactForm, text="Name", font=('arial', 14), bd=5)
    lbl_name.grid(row=0, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=1, sticky=W)
    lbl_address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
    lbl_address.grid(row=2, sticky=W)
    lbl_contact = Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
    lbl_contact.grid(row=3, sticky=W)
    lbl_email = Label(ContactForm, text="email", font=('arial', 14), bd=5)
    lbl_email.grid(row=4, sticky=W)
    lbl_qualification = Label(ContactForm, text="Qualification", font=('arial', 14), bd=5)
    lbl_qualification.grid(row=5, sticky=W)
    lbl_skills = Label(ContactForm, text="SKILLS", font=('arial', 14), bd=5)
    lbl_skills.grid(row=6, sticky=W)
    lbl_department = Label(ContactForm, text="Department", font=('arial', 14), bd=5)
    lbl_department.grid(row=7, sticky=W)
    lbl_work = Label(ContactForm, text="work", font=('arial', 14), bd=5)
    lbl_work.grid(row=8, sticky=W)

    #===================ENTRY===============================#
    name = Entry(ContactForm, textvariable=NAME, font=('arial', 14))
    name.grid(row=0, column=1)
    RadioGroup.grid(row=1, column=1)
    address = Entry(ContactForm, textvariable=ADDRESS,  font=('arial', 14))
    address.grid(row=2, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT,  font=('arial', 14))
    contact.grid(row=3, column=1)
    email = Entry(ContactForm, textvariable=EMAIL, font=('arial', 14))
    email.grid(row=4, column=1)
    qualification = Entry(ContactForm, textvariable=QUALIFICATION, font=('arial', 14))
    qualification.grid(row=5, column=1)
    department = Entry(ContactForm, textvariable=DEPARTMENT, font=('arial', 14))
    department.grid(row=6, column=1)
    skills = Entry(ContactForm, textvariable=SKILLS,  font=('arial', 14))
    skills.grid(row=7, column=1)
    work = Entry(ContactForm, textvariable=WORK, font=('arial', 14))
    work.grid(row=8, column=1)

    #==================BUTTONS==============================#
    btn_addcon = Button(ContactForm, text="Save", width=50,border = "10",activebackground="orange", command=SubmitData)
    btn_addcon.grid(row=9, columnspan=2, pady=10)

#============================FRAMES======================================#
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500 )
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370)
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
#============================LABELS======================================#
lbl_title = Label(Top, text="Employee Contact Management System", font=('arial', 16), width=500,background="orange")
lbl_title.pack(fill=X)

#============================ENTRY=======================================#

#============================BUTTONS=====================================#
btn_add = Button(MidLeft, text="ADD", bg="#66ff66",border = "10",activebackground="orange",width=40,height=5, command=AddNewWindow)
btn_add.pack()
btn_delete = Button(MidRight, text="REMOVE", bg="red",border = "10",activebackground="orange",width=40,height=5, command=DeleteData)
btn_delete.pack(side=RIGHT)

#============================TABLES======================================#

scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("MemberID", "name", "Gender",  "Address", "Contact", "qualification", "Skills","department" ,"email","work"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
style = ttk.Style()
style.configure("Treeview.Heading",foreground="blue",background="orange", font=(None, 12,'bold'))
style.configure("Treeview.column",fieldbackground="green")
tree.heading('MemberID', text="MemberID", anchor=W)
tree.heading('name', text="Name", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Contact', text="Contact", anchor=W)
tree.heading('qualification', text="Qualification", anchor=W)
tree.heading('Skills', text="Skills", anchor=W)
tree.heading('department', text="Department", anchor=W)
tree.heading('email', text="email", anchor=W)
tree.heading('work', text="work", anchor=W)

tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=120)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=120)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.column('#8', stretch=NO, minwidth=0, width=120)
tree.column('#9', stretch=NO, minwidth=0, width=120)
tree.column('#10', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)


# INITIALIZATION #
if __name__ == '__main__':
    Database()  
    root.mainloop()