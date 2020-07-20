# PROGRAM FOR  BASIC FILE HANDILNG
while True:
    print("//******** Telephone Directory********//")

    print("1:Create Contact")
    print("2:Read the contact")
    print("3:Search the contact number")
    print("4:Delete the contacts")
    print("5:exit")
    ch=int(input("Enter the choice : "))


    if ch==1:
        f=open("contact1.txt","a")
        name=input("Enter name:")
        name1 = name.lower()
        cno=input("Enter the contact number:")
        lc=len(cno)
        if lc>11:
            print("Enter 10 digits for mobile and 11 digits for landline,try again")
            # break
        else:
            data=name1+":"+cno+"\n"
            f.write(data)
        f.close()

    if ch==2:
        f=open("contact1.txt","r")
        rd=f.read()
        print(rd)
        f.close()

    if ch==3:
        s1=input("Enter the Name:")
        s=s1.lower()
        f=open("contact1.txt","r")
        x=f.readlines()
        for i in x:
               y=i
               p,q=y.split(":")
               if s==p or s==q:
                   print("Contact is present")
                   print("{}:{}".format(p,q))
                   break
        else:
            print("No such contact")
    if ch==4:
        print("1:Delete all contact")
        print("2:Single contact")
        ch1=input("Enter choice:")
        ch1=int(ch1)
        
        if ch1==1:
            print("1:Yes")
            print("2:No")
            A=int(input("Are you sure:"))
            if A==1:
                f=open("contact1.txt","w+")
                f.write(" ")
                f.close()
                break
            if A==2:
                break
        if ch1==2:
            s1=input("Enter the name:-")
            s = s1.lower()
            f=open("contact1.txt","r")
            y=f.readlines()
            f.close()
            length=len(y)
            for i in range(0,length,1):
                x=y[i]
                p,q=x.split(":")
                if s==p or s==q:
                    del y[i]
                    values=y
                    llll=len(values)
                    
                    f=open("contact2.txt","w")
                    a=f.writelines(values)
                    f.close()
                    with open("contact2.txt") as f:
                        with open("contact1.txt","w") as f1:
                            for line in f:
                                f1.write(line)
                    
                    break
                        
    if ch==5:

        break


    
