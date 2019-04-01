from Tkinter import *
import pymysql
import threading
def insert():
 #connection with the database1
    z=int(e1.get()) 
    x=e2.get()
    m=e3.get()
    n=e4.get()
    l=int(e5.get())
    k=(e6.get())
    p=e7.get()
    connect=pymysql.connect(host="localhost",user="akshita",passwd="Super_10",db="Bankdb")
    cur=connect.cursor()
 #Inserting data in the database
    sql_command="INSERT INTO entries values(%s,%s,%s,%s,%s,%s,%s)"
    data=(int(z),x,m,n,l,k,p)
    try:
        cur.execute(sql_command,data)
    except:
        print "<Error: Account name already Exist>" 
    #print z,x,m,n,l,k,p
    connect.commit()
    connect.close()
    
def SignIn(): #Signin function
   def Login():#subfunction1
 #connection with the database2
      z=int(s1.get()) 
      x=s2.get()
      connect=pymysql.connect(host="localhost",user="akshita",passwd="Super_10",db="Bankdb")
      cur=connect.cursor()
 # User Info      
      try:
        sql_command="select * from entries where Accountno=%s and Password=%s"  
        cur.execute(sql_command,(z,x))
        data=cur.fetchall()
        if data==():
          print "<Error> Either Accountno. or Password is incorrect"
        else:    
          print data
      except:
          print "Error in program Execution"  
      connect.commit()
      connect.close()
   def Tmoney():#subfunction2
    def money():
        #Connection with database3
        M=int(l1.get())
        N=int(l2.get())
        T=int(l3.get())
        connect=pymysql.connect(host="localhost",user="akshita",passwd="Super_10",db="Bankdb")
        cur=connect.cursor()
 #Money transfer program
        r="Select Totalbalance from entries where Accountno=%s"
        cur.execute(r,(N))
        data=cur.fetchall()
        data=int(data[0][0])+T
        print data
        I="update entries set Totalbalance=%s where Accountno=%s"
        cur.execute(I,(data,N))
        K="Select Totalbalance from entries where Accountno=%s"
        cur.execute(K,(M))
        data1=cur.fetchall()
        print data1
        data1=int(data1[0][0])-T
        print data1
        Q="update entries set Totalbalance=%s where Accountno=%s"
        cur.execute(Q,(data1,M))
        connect.commit()
        connect.close()
    
  
    #Transfer money page
    Tmoney = Tk()
    Tmoney.title("SignIn")
    A=Label(Tmoney, text="From Account")
    G=Label(Tmoney, text="To Account")
    O=Label(Tmoney, text="Money to Transfer")
   

    A.grid(row=0,column=0)
    G.grid(row=1,column=0)
    O.grid(row=2,column=0)
    l1=Entry(Tmoney)
    l2=Entry(Tmoney)
    l3=Entry(Tmoney)
    l1.grid(row=0,column=1)
    l2.grid(row=1,column=1)
    l3.grid(row=2,column=1)
    W=Button(Tmoney,text="Quit",fg="Red",command=Tmoney.destroy)
    D=Button(Tmoney,text="Transfer money",fg="Yellow",command=money)
    W.grid(row=3, column=0)
    D.grid(row=3,column=2)
    Signin.destroy()
    Tmoney.mainloop()
# Signin form
   Signin = Tk()
   Signin.title("Signin")
   A=Label(Signin, text="Account no.")
   G=Label(Signin, text="Password")

   A.grid(row=0,column=0)
   G.grid(row=1,column=0)
   s1=Entry(Signin)
   s2=Entry(Signin,show="*")
   s1.grid(row=0,column=1)
   s2.grid(row=1,column=1)
   Q=Button(Signin,text="Login",fg="Blue",command=Login) 
   W=Button(Signin,text="Quit",fg="Red",command=Signin.destroy)
   D=Button(Signin,text="Transfer money",command=Tmoney)
   W.grid(row=2, column=0)
   Q.grid(row=2,column=2)
   D.grid(row=2,column=1)
   window.destroy()
   Signin.mainloop()
    
#Registration form
window = Tk()
window.title("Registration form")
A=Label(window, text="Account no.")
B=Label(window, text="Name")
C=Label(window, text="Fathersname")
D=Label(window, text="Date of birth")
E=Label(window, text="Total money")
F=Label(window, text="Branch")
G=Label(window, text="Password")

A.grid(row=0,column=0)
B.grid(row=1,column=0)
C.grid(row=2,column=0)
D.grid(row=3,column=0)
E.grid(row=4,column=0)
F.grid(row=5,column=0)
G.grid(row=6,column=0)
e1=Entry(window)
e2=Entry(window)
e3=Entry(window)
e4=Entry(window)
e5=Entry(window)
e6=Entry(window)
e7=Entry(window,show="*")
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)
e6.grid(row=5,column=1)
e7.grid(row=6,column=1)
Q=Button(window,text="Save",fg="Blue",command=insert) 
W=Button(window,text="Quit",fg="Red",command=window.destroy)
M=Button(window,text="SignIn",fg="Green",command=SignIn)
W.grid(row=7, column=1)
M.grid(row=7,column=2)
Q.grid(row=7,column=0)
window.mainloop()
    
   
