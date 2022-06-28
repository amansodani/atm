import mysql.connector
mydb=mysql.connector.connect(host="127.0.0.1",user='root',password='mitochondria',database='newuser',auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

import tkinter
window = tkinter.Tk()
window.title("ATM")
window.geometry("510x600")
passw=tkinter.IntVar()
passw.set("")
name=tkinter.StringVar()
passw1=tkinter.IntVar()
passw1.set("")
deposit=tkinter.StringVar()
withdraw=tkinter.IntVar()
withdraw.set("")
def mini():
    icon1 = tkinter.PhotoImage(file="WBC3.png")
    label = tkinter.Label(window, image=icon1)
    label.place(x=0, y=0, width=510, height=600)
    button6 = tkinter.Button(window, text="<-back", font="Ebrima 20 bold", command=submit).place(x=0, y=0, width=150,height=50)
    window.configure(bg="blue")
    window.mainloop()
def enq():
    icon1 = tkinter.PhotoImage(file="WBC7.png")
    label = tkinter.Label(window, image=icon1)
    label.place(x=0, y=0, width=510, height=600)
    mycursor.execute("SELECT deposit FROM newuser")
    myresult1 = mycursor.fetchall()
    amt=myresult1[a-1][0]
    amt=str(amt)

    text=tkinter.Label(text=amt,font="Ebrima 20 bold").place(x=230, y=300, width=150,height=80)
    button6 = tkinter.Button(window, text="<-back", font="Ebrima 20 bold", command=submit).place(x=0, y=0, width=150,height=50)
    window.configure(bg="blue")
    window.mainloop()
def A():
    mycursor.execute("SELECT deposit FROM newuser")
    myresult1 = mycursor.fetchall()
    amt = myresult1[a - 1][0]
    amt = amt - 500
    if amt>=0 :
        mycursor.execute('''
                       UPDATE newuser.newuser
                       SET deposit = %s
                       WHERE password=%s''', (amt, y))
        icon1 = tkinter.PhotoImage(file="WBC6.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
    else:
        icon1 = tkinter.PhotoImage(file="WBC8.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
    window.mainloop()

def B():
    mycursor.execute("SELECT deposit FROM newuser")
    myresult1 = mycursor.fetchall()
    amt = myresult1[a - 1][0]
    amt = amt - 1000
    if amt>=0 :

        mycursor.execute('''
                    UPDATE newuser.newuser
                    SET deposit = %s
                    WHERE password=%s''', (amt, y))
        icon1 = tkinter.PhotoImage(file="WBC6.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
    else:
        icon1 = tkinter.PhotoImage(file="WBC8.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
    window.mainloop()

def C():
    mycursor.execute("SELECT deposit FROM newuser")
    myresult1 = mycursor.fetchall()
    amt = myresult1[a - 1][0]
    amt = amt - 2000
    if amt>=0 :
        mycursor.execute('''
                       UPDATE newuser.newuser
                       SET deposit = %s
                       WHERE password=%s''', (amt, y))
        icon1 = tkinter.PhotoImage(file="WBC6.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
    else:
        icon1 = tkinter.PhotoImage(file="WBC8.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
    window.mainloop()

def D():
    mycursor.execute("SELECT deposit FROM newuser")
    myresult1 = mycursor.fetchall()
    amt = myresult1[a - 1][0]
    amt = amt - 5000
    if amt>=0 :
        mycursor.execute('''
                    UPDATE newuser.newuser
                    SET deposit = %s
                    WHERE password=%s''', (amt, y))
        icon1 = tkinter.PhotoImage(file="WBC6.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
    else:
        icon1 = tkinter.PhotoImage(file="WBC8.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
    window.mainloop()

def E():
    mycursor.execute("SELECT deposit FROM newuser")
    myresult1 = mycursor.fetchall()
    amt = myresult1[a - 1][0]
    amt = amt - 10000
    if amt>=0 :
        mycursor.execute('''
                       UPDATE newuser.newuser
                       SET deposit = %s
                       WHERE password=%s''', (amt, y))
        icon1 = tkinter.PhotoImage(file="WBC6.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
    else:
        icon1 = tkinter.PhotoImage(file="WBC8.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
    window.mainloop()

def F():
    mycursor.execute("SELECT deposit FROM newuser")
    myresult1 = mycursor.fetchall()
    amt = myresult1[a - 1][0]
    amt = amt - 20000
    if amt>=0 :
        mycursor.execute('''
                    UPDATE newuser.newuser
                    SET deposit = %s
                    WHERE password=%s''', (amt, y))
        icon1 = tkinter.PhotoImage(file="WBC6.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
    else:
        icon1 = tkinter.PhotoImage(file="WBC8.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
    window.mainloop()


def completed():
    icon1 = tkinter.PhotoImage(file="WBC6.png")
    label = tkinter.Label(window, image=icon1)
    label.place(x=0, y=0, width=510, height=600)
    window.mainloop()
def complete():
    w=withdraw.get()
    icon1 = tkinter.PhotoImage(file="WBC6.png")
    label = tkinter.Label(window, image=icon1)
    label.place(x=0, y=0, width=510, height=600)
    mycursor.execute("SELECT deposit FROM newuser")
    myresult1 = mycursor.fetchall()
    amt = myresult1[a - 1][0]
    amt = amt-w
    if amt >=0 :
        mycursor.execute('''
                    UPDATE newuser.newuser
                    SET deposit = %s
                    WHERE password=%s''',(amt,y))
    else :
        icon1 = tkinter.PhotoImage(file="WBC8.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
    window.mainloop()
def comp():

    icon1 = tkinter.PhotoImage(file="WBC6.png")
    label = tkinter.Label(window, image=icon1)
    label.place(x=0, y=0, width=510, height=600)
    window.mainloop()
def amountw():
    icon1 = tkinter.PhotoImage(file="WBC3.png")
    label = tkinter.Label(window, image=icon1)
    label.place(x=0, y=0, width=510, height=600)
    tex = tkinter.Button(window, text="PLEASE ENTER AMOUNT", font="Ebrima 20 bold").place(x=25, y=100,width=460,height=100)
    ent2 = tkinter.Entry(window, font=("Roman 30 bold"), textvariable=withdraw).place(x=110, y=300, width=300, height=50)

    button4 = tkinter.Button(window, text="NO", font="Ebrima 20 bold",command=comp).place(x=350, y=500, width=150, height=50)
    button5 = tkinter.Button(window, text="YES", font="Ebrima 20 bold",command=complete).place(x=350, y=420, width=150, height=50)
    button6 = tkinter.Button(window, text="<-back", font="Ebrima 20 bold", command=cashw).place(x=0, y=0, width=150,height=50)
    window.configure(bg="blue")
    window.mainloop()
def cashw():
    icon1 = tkinter.PhotoImage(file="WBC3.png")
    label = tkinter.Label(window, image=icon1)
    label.place(x=0, y=0, width=510, height=600)
    button3 = tkinter.Button(window, text="CREDIT", font="Ebrima 20 bold",command=amountw).place(x=350, y=100, width=150,height=50)
    button4 = tkinter.Button(window, text="CURRENT", font="Ebrima 20 bold",command=amountw).place(x=350, y=260, width=150,height=50)
    button5 = tkinter.Button(window, text="SAVINGS", font="Ebrima 20 bold",command=amountw).place(x=350, y=420, width=150,height=50)
    button6 = tkinter.Button(window, text="<-back", font="Ebrima 20 bold", command=submit).place(x=0, y=0,width=150,height=50)
    window.configure(bg="blue")
    window.mainloop()
def fastcash():
    button1 = tkinter.Button(window, text="500", font="Ebrima 20 bold",command=A).place(x=10, y=100, width=150,height=50)
    button2 = tkinter.Button(window, text="1000", font="Ebrima 20 bold",command=B).place(x=10, y=260, width=150, height=50)
    button3 = tkinter.Button(window, text="5000", font="Ebrima 20 bold",command=D).place(x=350, y=100,width=150,height=50)
    button4 = tkinter.Button(window, text="10000", font="Ebrima 20 bold",command=E).place(x=350, y=260, width=150,height=50)
    button5 = tkinter.Button(window, text="20000", font="Ebrima 20 bold",command=F).place(x=350, y=420, width=150,height=50)
    button6 = tkinter.Button(window, text="2000", font="Ebrima 20 bold",command=C).place(x=10,y=420,width=150,height=50)
    button6 = tkinter.Button(window, text="<-back", font="Ebrima 20 bold", command=submit).place(x=0, y=0, width=150,height=50)

def oldone():
    icon2 = tkinter.PhotoImage(file="WBC4.png")
    label1 = tkinter.Label(window, image=icon2)
    label1.place(x=0, y=0, width=510, height=600)
    window.mainloop()
def lost():
    icon2 = tkinter.PhotoImage(file="WBC5.png")
    label1 = tkinter.Label(window, image=icon2)
    label1.place(x=0, y=0, width=510, height=600)
    window.mainloop()
def cbr():
    icon1 = tkinter.PhotoImage(file="WBC3.png")
    label = tkinter.Label(window, image=icon1)
    label.place(x=0,y=0,width=510,height=600)
    tex=tkinter.Button(window,text="Why do you need a new\n Cheque Book ?",font="Ebrima 20 bold").place(x=20,y=100,width=460,height=100)
    tex1=tkinter.Button(window,text="1.Lost the old one \n Freeze my account",font="Ebrima 20 bold",command=lost).place(x=20,y=250,width=460,height=100)
    tex1 = tkinter.Button(window, text="2.Old one is filled completely", font="Ebrima 20 bold",command=oldone).place(x=20,y=400,width=460,height=100)
    button6 = tkinter.Button(window, text="<-back", font="Ebrima 20 bold", command=submit).place(x=0, y=0, width=150,height=50)
    window.configure(bg="blue")
    window.mainloop()
def submit():

    global y
    y = passw.get()
    mycursor.execute("SELECT password FROM newuser")
    myresult = mycursor.fetchall()
    temp=0
    global a
    a=0
    for x in myresult:
        a=a+1
        if x[0] ==y :
            temp=temp+1
            break
        else :
            continue
    if temp == 0 :
        wrong()
    else:
        icon1 = tkinter.PhotoImage(file="WBC3.png")
        label = tkinter.Label(window, image=icon1)
        label.place(x=0, y=0, width=510, height=600)
        button1 = tkinter.Button(window, text="MINI STATEMENT", font="Ebrima 10 bold",command=mini).place(x=10, y=100, width=150, height=50)
        button2 = tkinter.Button(window, text="PIN CHANGE", font="Ebrima 10 bold").place(x=10, y=260, width=150, height=50)
        button3 = tkinter.Button(window, text="FAST CASH", font="Ebrima 10 bold",command=fastcash).place(x=350, y=100, width=150,height=50)
        button4 = tkinter.Button(window,text="BALANCE ENQUIRY",font="Ebrima 10 bold",command=enq).place(x=350,y=260,width=150,height=50)
        button5 = tkinter.Button(window, text="CASH\n WITHDRAWL", font="Ebrima 10 bold",command=cashw).place(x=350, y=420, width=150,height=50)
        button6 = tkinter.Button(window, text="CHEQUE BOOK\nREQUIREMENT", font="Ebrima 10 bold",command=cbr).place(x=10, y=420, width=150, height=50)
        window.configure(bg="blue")
        window.mainloop()
def wrong():
    icon1 = tkinter.PhotoImage(file="WBC3.png")
    label = tkinter.Label(window, image=icon1)
    label.place(x=0, y=0, width=510, height=600)
    text = tkinter.Label(text="Incorrect Password", font="Ebrima 20 bold").place(x=50, y=250, width=400, height=100)
    window.configure(bg="blue")
    window.mainloop()
def newuser():
    icon1 = tkinter.PhotoImage(file="WBC3.png")
    label = tkinter.Label(window, image=icon1)
    label.place(x=0, y=0, width=510, height=600)
    ent2=tkinter.Entry(window,font=("Roman 30 bold"),textvariable=name).place(x=200,y=100,width=300,height=50)
    ent3 = tkinter.Entry(window, font=("Roman 30 bold"),show=('*'), textvariable=passw1).place(x=200, y=260, width=300, height=50)
    ent4 = tkinter.Entry(window, font=("Roman 30 bold"), textvariable=deposit).place(x=200, y=410, width=300, height=50)
    button1 = tkinter.Button(window, text="Name", font="Ebrima 10 bold").place(x=20, y=100, width=150, height=50)
    button2 = tkinter.Button(window, text="Password", font="Ebrima 10 bold").place(x=20, y=260, width=150, height=50)
    button3 = tkinter.Button(window, text="Amount Deposit", font="Ebrima 10 bold").place(x=20, y=410, width=150, height=50)
    button4=tkinter.Button(window,text="Done",font="Ebrima 20 bold",command=done).place(x=160,y=500,width=200,height=50)
    window.configure(bg="blue")
    window.mainloop()


def done():
    y = name.get()
    x = passw1.get()
    z = deposit.get()
    sql = "INSERT INTO newuser(password,name,deposit) VALUES(%s,%s,%s)"
    val =(x,y,z)
    mycursor.execute(sql,val)
    mydb.commit()
    icon1 = tkinter.PhotoImage(file="WBC2.png")
    label = tkinter.Label(window, image=icon1)
    label.place(x=0, y=0, width= 510,height=600)
    window.configure(bg="white")
    window.mainloop()

def start():
    icon=tkinter.PhotoImage(file = "WBC.png")
    label1=tkinter.Label(window,image=icon)
    label1.pack()
    ent1 = tkinter.Entry(window,font=("Roman 80 bold"),textvariable=passw,show ='*')
    label2=ent1
    label2.place(x = 306,y = 500,width=200,height=100)
    sub=tkinter.Button(window,text='Submit',font="Ebrima 20 bold",bg="yellow",command=submit)
    label3=sub
    label3.place(x=305,y=550,width=200,height=50)
    icon1=tkinter.PhotoImage(file="WBC1.png")
    label=tkinter.Label(window,image=icon1)
    label.place(x=4,y=501)
    button=tkinter.Button(window,text="New User",font = "Ebrima 10 bold",bg ="yellow",command=newuser)
    label4=button
    label4.place(x=4,y=0,width=100,height=50)
    window.mainloop()
start()
mydb.commit()
window.mainloop()





