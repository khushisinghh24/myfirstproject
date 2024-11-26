def hsms():
    import mysql.connector as sql
    mycon=sql.connect(host='localhost',user='root',password='12345678',database='hubnetdb')
    mycur=mycon.cursor()
    print("\t\t------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\tWelcome to Hubnet")
    print("\t\t------------------------------------------------------------------------------------------")
    ch=int(input("\t\t\tPress 1 for Login or Press 2 for SignUP : "))
    if ch==1:
        print("\n\t\t\t\tUser Login")
        uid=input("\n\t\t\tEnter UserID     :   ")
        pas=input("\t\t\tEnter Password   :   ")
        q="select userid,password from users where userid='{}' and password='{}'".format(uid,pas)
        mycur.execute(q)
        data=mycur.fetchall()
        if data==[]:
            print("Login Fail because invalid userid or password!!!")
        else:
            print("\t\t------------------------------------------------------------------------------------------")
            print("\t\t\t\t\tWelcome to Hubnet Student Management System")
            print("\t\t------------------------------------------------------------------------------------------")
            print("\t\t\t1. Press 1 For New Entry of Student  : ")
            print("\t\t\t2. Press 2 For Student Verification  : ")
            print("\t\t\t3. Press 3 To Update Student Details : ")
            print("\t\t\t4. Press 4 To Delete Student Record  : ")
            print("\t\t\t5. Press 5 To Close the Application  : ")
            chh=int(input("\t\t\tEnter Your Choice : "))
            if chh==1:
                sid=input("Enter Student ID  : ")
                sname=input("Enter Student name : ")
                dob=input("Enter Date of Birth : ")
                phone=input("Enter Phone Number : ")
                doa=input("Enter Date of Admission : ")
                cid=input("Enter Course ID  : ")
                q="insert into student values('{}','{}','{}','{}','{}','{}')".format(sid,sname,dob,phone,doa,cid)
                mycur.execute(q)
                mycon.commit()
                print("Record Saved Successfully!!!")
            elif chh==2:
                sid=input("Enter Student ID  : ")
                q1="select sid from student where sid='{}'".format(sid)
                mycur.execute(q1)
                ssid=str(mycur.fetchall())
                q2="select sname from student where sid='{}'".format(sid)
                mycur.execute(q2)
                sname=str(mycur.fetchall())
                q3="select dob from student where sid='{}'".format(sid)
                mycur.execute(q3)
                dob=str(mycur.fetchall())
                q4="select phone from student where sid='{}'".format(sid)
                mycur.execute(q4)
                phone=str(mycur.fetchall())
                q5="select doa from student where sid='{}'".format(sid)
                mycur.execute(q5)
                doa=str(mycur.fetchall())
                q6="select cid from student where sid='{}'".format(sid)
                mycur.execute(q6)
                cid=str(mycur.fetchall())
                
                if data==[]:
                    print("Record Not Found!!")
                else:
                    print("Record Found : ")
                    print("SID\t\tNAME\t\tDATE OF BIRTH\t\tPhoneNumber\t\tDATE OF ADMISSION\t\tCourseID")
                    print(ssid,"\t",sname,"\t",dob,"\t",phone,"\t",doa,"\t",cid)
            elif chh==3:
                chhh=int(input("Press 1 to update phone no or press 2 to update course id : "))
                if chhh==1:
                    sid=input("Enter Student ID : ")
                    npn=input("Enter New Phone Number : ")
                    q="update student set phone='{}' where sid='{}'".format(npn,sid)
                    mycur.execute(q)
                    mycon.commit()
                    print("Phone Number updated SuccessFully!!!")
                elif chhh==2:
                    sid=input("Enter Student ID : ")
                    nci=input("Enter New Course ID : ")
                    q="update student set cid='{}' where sid='{}'".format(nci,sid)
                    mycur.execute(q)
                    mycon.commit()
                    print("Course ID updated SuccessFully!!!")
                         
            elif chh==4:
                sid=input("Enter Student ID : ")
                q="select * from student where sid='{}'".format(sid)
                qq="delete from student where sid='{}'".format(sid)
                mycur.execute(q)
                data=mycur.fetchall()
                if data==[]:
                    print("No record found to be deleted!!!")
                else:
                    mycur.execute(qq)
                    mycon.commit()
                    print("One Record Deleted!!!")
            elif chh==5:
                exit(1)
    elif ch==2:
        print("\n\t\t\t\tUser SignUP")
        uid=input("\n\t\t\tEnter UserID     :   ")
        pas=input("\t\t\tEnter Password   :   ")
        q="insert into users values ('{}','{}')".format(uid,pas)
        mycur.execute(q)
        mycon.commit()
        print("User SignUp Successfully!!!")
    cch=int(input("Would you like to continue with this application press 1 for yes : "))
    if cch==1:
        hsms()
    else:
        print("Good Luck!!!")

hsms()
