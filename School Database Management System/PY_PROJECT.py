import mysql.connector as mp
c=mp.connect(host='localhost',user='root',passwd='Sumit@213',database='kv_cossipore')
cur=c.cursor()

#main screen of database
#python_interface


#___________________________________________
def login_screen():
    s="select * from staff;"
    cur.execute(s)
    data=cur.fetchall()
    print("Alert !!")
    print("inputting incorrect user id and password may lead to shutting down of software:")
    print()
    si=input("\t\t\tEnter User Id:_")
    pw=input("\t\t\tEnter Password:_")
    print()
    for r in data:
        if r[0]==si and r[5]==pw:
            print('Hello !',r[1])
            print()
            print('The',r[2],'of this school')
            print()
            print('Welcome to School database of kv_cossipore !')
            print()
            display()
            break       
    else:
        print("incorrect user id and password !!")
        print()
        tu=input("WANT TO TRY AGAIN ?(Y/N):_")
        print()
        if tu=='y' or tu=='Y':
            login_screen()
        else:
            exit()
#_____________________________________________________________________
        
#working___________________________________________________________
            
def view_details():
    print('want to see details of -->')
    print("1. Teachers")
    print("2. Students")
    print()
    print("3. want to go to previous menu ?")
    print()
    bh=int(input('enter one of the above choices(enter only the number !):_'))
    if bh==1:
        print()
        vd_teach()
    elif bh==2:
        print()
        vd_stud()
    elif bh==3:
        display()
    else:
        gk=input("want to restart the program ?(Y/N):_ !")
        if gk=='Y' or gk=='y':
            display()
        else:
            exit()
            
def insert_details():
    print('want to register details of -->')
    print()
    print('1. A Teacher')
    print('2. A Student')
    print()
    print('3.want to go to previous menu....')
    print()
    bh=int(input("enter among following choices(enter only the number !):_"))
    if bh==1:
        print()
        id_teach()
    elif bh==2:
        id_stud()
    elif bh==3:
        display()
    else:
        gk=input("want to restart the program ?(Y/N):_ !")
        if gk=='Y' or gk=='y':
            display()
        else:
            exit()

def update_details():
    print("want to update details of -->")
    print()
    print("1. Teacher")
    print("2. Student")
    print()
    print("3. want to go to previous menu....")
    print()
    bh=int(input("enter from above choices(enter only the number !):_"))
    if bh==1:
        ud_teach()
    elif bh==2:
        ud_stud()
    elif bh==3:
        display()
    else:
        gk=input("want to restart the program ?(Y/N):_ !")
        if gk=='Y' or gk=='y':
            display()
        else:
            exit()

def remove_details():
     print("want to remove details of -->")
     print()
     print("1. A Teacher")
     print("2. A Student")
     print()
     print("3. want to go to previous menu....")
     print()
     bh=int(input("enter among following choices(enter only the number !):_"))
     if bh==1:
        rd_teach()
     elif bh==2:
        rd_stud()
     elif bh==3:
        display()
     else:
         gk=input("want to restart the program ?(Y/N):_ !")
         if gk=='Y' or gk=='y':
             display()
         else:
             exit()
        
def display():
    print()
    print('Following things can be done using this DBMS sofware of KENDRIYA VIDYALAYA COSSIPORE --> ')
    print()
    print('1. to see details')
    print('2. to register details')
    print('3. to update details')
    print('4. to remove details')
    print('5. exit')
    print()
    ch=int(input("enter any one of the options above(enter only the number !):_"))
    print()
    if ch==1:
        view_details()
    elif ch==2:
        insert_details()
    elif ch==3:
        update_details()
    elif ch==4:
        remove_details()
    elif ch==5:
        exit()
    else:
        print("you have inputted an incorrect choice")
        print("choose among the following -->")
        print("1. restarting the program once again...")
        print("2.closing the program:")
        hd=int(input("enter your choice:"))
        if hd==1:
            display()
        else:
            exit()       
def vd_stud():
    print()
    print('want to search details of student studying in -->')
    print()
    print("1.  class XII")
    print("2.  class XI")
    print("3.  class X")
    print("4.  class IX")
    print("5.  class VIII")
    print("6.  class VII")
    print("7.  class VI")
    print("8.  class V")
    print("9.  class IV")
    print("10. class III")
    print("11. class II")
    print("12. class I")
    print()
    print("13. Want to go to previous menu ?")
    print()
    mh=int(input("enter among following choices(enter only the number !):_"))
    print()
    if mh==1:
        x1='SELECT * FROM STUDENT_DETAILS  where class like "XII%" order by adm_no;'
    elif mh==2:
        x1='SELECT * FROM STUDENT_DETAILS  where class like "XI %" order by adm_no;'
    elif mh==3:
        x1='SELECT * FROM STUDENT_DETAILS  where class like "X %" order by adm_no;'
    elif mh==4:
        x1='SELECT * FROM STUDENT_DETAILS  where class like "IX %" order by adm_no;'
    elif mh==5:
        x1='SELECT * FROM STUDENT_DETAILS  where class like "VIII %" order by adm_no;'
    elif mh==6:
        x1='SELECT * FROM STUDENT_DETAILS  where class like "VII %" order by adm_no;'
    elif mh==7:
        x1='SELECT * FROM STUDENT_DETAILS  where class like "VI %" order by adm_no;'
    elif mh==8:
        x1='SELECT * FROM STUDENT_DETAILS  where class like "V %" order by adm_no;'
    elif mh==9:
        x1='SELECT * FROM STUDENT_DETAILS  where class like "IV %" order by adm_no;'
    elif mh==10:
        x1='SELECT * FROM STUDENT_DETAILS  where class like "III %" order by adm_no;'
    elif mh==11:
        x1='SELECT * FROM STUDENT_DETAILS  where class like "II %" order by adm_no;'
    elif mh==12:
        x1='SELECT * FROM STUDENT_DETAILS  where class like "I %" order by adm_no;'
    elif mh==13:
        view_details()
    else:
        gk=input("want to restart the program ?(Y/N):_ ")
        if gk=='Y' or gk=='y':
            display()
        else:
            exit()
        
    cur.execute(x1)
    data=cur.fetchall()
    for r in data:
        print("admission _no:",r[0],' || ',"name_of_student:",r[1],' || ',"roll_no:",r[2],' || ',"class:",r[3],' || ',"contact_details:",r[4])
        print()
    print("the data presented to you is sorted according to their admission no. in ascending order")
    print()
    print()
    print("choose among the following -->")
    print()
    print("1.want to restart the program again from begining")
    print("2.want to go to previos menu.....")
    print("3.want to close the program:")
    print()
    qd=int(input("enter your choice(enter only the number !):_"))
    if qd==1: 
        display()
    elif qd==2:
        view_details()
    else:
        exit()
    vd_stud()

def vd_teach():
    print()
    print("want to see details of:-->")
    print()
    print("1. chemistry_teachers")
    print("2. computer_teachers")
    print("3. commerce_teachers")
    print("4. english_teachers")
    print("5. maths_teachers")
    print("6. physics_teachers")
    print("7. hindi_teachers")
    print("8. art_teachers")
    print()
    print("9. want to go to previous menu...")
    print()
    df=int(input("enter among following choices(enter only the number !):_"))
    if df==1:
        xa='select * from teacher_details where post like "%chemistry" order by date_of_joining;'
    elif df==2:
        xa='select * from teacher_details where post like "%computer" order by date_of_joining;'
    elif df==3:
        xa='select * from teacher_details where post like "%commerce" order by date_of_joining;'
    elif df==4:
        xa='select * from teacher_details where post like "%english" order by date_of_joining;'
    elif df==5:
        xa='select * from teacher_details where post like "%maths" order by date_of_joining;'
    elif df==6:
        xa='select * from teacher_details where post like "%physics" order by date_of_joining;'
    elif df==7:
        xa='select * from teacher_details where post like "%hindi" order by date_of_joining;'
    elif df==8:
        xa='select * from teacher_details where post like "%art" order by date_of_joining;'
    elif df==9:
        view_details()
    else:
        gk=input("want to restart the program ?(Y/N):_ ")
        if gk=='Y' or gk=='y':
            display()
        else:
            exit()
        
    cur.execute(xa)
    data=cur.fetchall()
    for r in data:
        print("Teacher_id:",r[0],' || ',"Name_of_Teacher:",r[1],' || ',"Post:",r[2],' || ',"Date_of_Joining:",r[3],' || ',"Salary:",r[4])
        print()
    print("The data presented to you is sorted in according to their joining date in acsending order")
    print()
    print()
    print("choose among the following -->")
    print()
    print("1.want to restart the program again from begining")
    print("2.want to go to previos menu.....")
    print("3.want to close the program:")
    print()
    qd=int(input("enter your choice(enter only the number !):_"))
    if qd==1: 
        display()
    elif qd==2:
        view_details()
    else:
        exit()      
    vd_teach()

def id_teach():
    print()
    print("to register details of a new teacher in the school database of kv_cossipore.....")
    print("you need to submit the following details !!:")
    print()
    xe=str(input("enter teacher id:_"))
    xf=str(input("enter name of teacher:_"))
    xg=str(input("enter post of teacher:_"))
    xh=str(input("enter date of joining:_"))
    xj=int(input("enter salary of teacher:_"))
    q="insert into teacher_details(teacher_id, name_of_teacher, post, date_of_joining, salary)values('{}','{}','{}','{}',{})".format(xe,xf,xg,xh,xj)
    cur.execute(q)
    c.commit()
    print()
    print("inputted details of the given teacher has been succesfully registered !")
    print()
    print("choose among the following -->")
    print()
    print("1.want to restart the program again from begining")
    print("2.want to go to previos menu.....")
    print("3.want to close the program:")
    print()
    qd=int(input("enter your choice(enter only the number !):_"))
    if qd==1: 
        display()
    elif qd==2:
        insert_details()
    else:
        exit()
    id_teach()


def id_stud():
    print()
    print("to register details of a new student in the school database of kv_cossipore.....")
    print("you need to submit the following details: !!")
    print()
    ze=int(input("enter admission number of student:_"))
    zr=str(input("enter name of student:_"))
    zt=int(input("enter roll number of the student:_"))
    zy=str(input("enter class of the student:_"))
    zu=int(input("enter only 10 digit contact phone number:_"))
    qs="insert into student_details(adm_no,student_name,roll_no,class,contact)values({},'{}',{},'{}',{})".format(ze,zr,zt,zy,zu)
    cur.execute(qs)
    c.commit()
    print()
    print("inputted details of the given student has been succesfullly registered !")
    print()
    print("choose among the following -->")
    print()
    print("1.want to restart the program again from begining")
    print("2.want to go to previos menu.....")
    print("3.want to close the program:")
    print()
    qd=int(input("enter your choice(enter only the number !):_"))
    if qd==1: 
        display()
    elif qd==2:
        insert_details()
    elif qd==3:
        exit()
    id_stud()

    
def ud_teach():
    print()
    tid=input("Enter the Teacher_id whose details you want to update :_")
    print()
    cur.execute("select * from teacher_details where teacher_id='{}'".format(tid))
    d=cur.fetchone()
    print(d[0],d[1],d[2],d[3],d[4])
    print("What do you want to update ?")
    print()
    print("1.Post_of_the_teacher")
    print("2.Date_of_Joining_of_teacher")
    print("3.Salary_of_teacher")
    print()
    x=int(input("choose among the following options(enter only the number !)"))
    print()
    if x== 1:
        pp=input("Enter the new post of the teacher:_")
        st="update teacher_details set post='{}' where teacher_id='{}'".format(pp,tid)
        cur.execute(st)
        c.commit()
    elif x==2:
        doj=input("Enter the new date of joining of teacher:_")
        st="update teacher_details set date_of_joining='{}' where teacher_id='{}'".format(doj,tid)
        cur.execute(st)
        c.commit()
    elif x==3:
        sal=int(input("Enter the new salary of the teacher:_"))
        st="update teacher_details set salary={} where teacher_id='{}'".format(sal,tid)
        cur.execute(st)
        c.commit()
    else:
        gk=input("want to restart the program ?(Y/N):_ ")
        if gk=='Y' or gk=='y':
            display()
        else:
            exit()
        
    print()
    print("the details of the given teacher has been succesfully updated !")
    print()
    print("choose among the following -->")
    print()
    print("1.want to restart the program again from begining")
    print("2.want to go to previos menu.....")
    print("3.want to close the program:")
    print()
    qd=int(input("enter your choice(enter only the number !):_"))
    if qd==1: 
        display()
    elif qd==2:
        update_details()
    else:
        exit()
    ud_teach()
        
def ud_stud():
    cf=int(input("enter admission number:"))
    print()
    cur.execute("select * from student_details where adm_no={}".format(cf))
    d=cur.fetchone()
    print(d[0],d[1],d[2],d[3],d[4])
    print("What do you want to update about yourself ?")
    print()
    print("1.Name_of_the_Student")
    print("2.Roll_number_of_student")
    print("3.Class_of_student")
    print("4.Contact_details_of_student")
    print()
    x=int(input("choose among the following options(enter only the number !)"))
    print()
    if x== 1:
        nm=input("Enter your new name:_")
        st="update student_details set student_name='{}' where adm_no={}".format(nm,cf)
        cur.execute(st)
        c.commit()
    elif x==2:
        rn=input("Enter your new roll number:_")
        st="update student_details set roll_no='{}' where adm_no={}".format(rn,cf)
        cur.execute(st)
        c.commit()
    elif x==3:
        cl=int(input("Enter your new class:_"))
        st="update teacher_details set class={} where adm_no={}".format(cl,cf)
        cur.execute(st)
        c.commit()
    elif x==4:
        cd=int(input("enter your new contact details:"))
        st="update student_details set contact={} where adm_no={}".format(cd,cf)
        cur.execute(st)
        c.commit()
    else:
        gk=input("want to restart the program ?(Y/N):_ ")
        if gk=='Y' or gk=='y':
            display()
        else:
            exit()
        
    print()
    print("the details of the given student has been succesfully updated !")
    print()
    print("choose among the following -->")
    print()
    print("1.want to restart the program again from begining")
    print("2.want to go to previos menu.....")
    print("3.want to close the program:")
    print()
    qd=int(input("enter your choice(enter only the number !):_"))
    if qd==1: 
        display()
    elif qd==2:
        update_details()
    else:
        exit()
    ud_stud()

    
def rd_teach():
    tid=str(input("Enter the teacher_id of the teacher whose details you want to remove:"))
    st="delete from teacher_details where teacher_id='{}'".format(tid)
    cur.execute(st)
    c.commit()
    print()
    print("the details of the given teacher has been succesfully removed !")
    print()
    print("choose among the following -->")
    print()
    print("1.want to restart the program again from begining")
    print("2.want to go to previos menu.....")
    print("3.want to close the program:")
    print()
    qd=int(input("enter your choice(enter only the number !):_"))
    if qd==1: 
        display()
    elif qd==2:
        remove_details()
    else:
        exit()
    rd_teach()

def rd_stud():
    adm=str(input("Enter the Admission number of the student whose details you want to remove:"))
    st="delete from student_details where adm_no='{}'".format(adm)
    cur.execute(st)
    c.commit()
    print()
    print("the details of the given student has been succesfully removed !")
    print()
    print("choose among the following -->")
    print()
    print("1.want to restart the program again from begining")
    print("2.want to go to previos menu.....")
    print("3.want to close the program:")
    print()
    qd=int(input("enter your choice(enter only the number !):_"))
    if qd==1: 
        display()
    elif qd==2:
        remove_details()
    else:
        exit()

#_main_
login_screen()
