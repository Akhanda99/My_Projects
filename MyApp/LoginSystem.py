from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter import simpledialog
login=Tk()
login.geometry("450x600")

login.iconbitmap(r"c:/Users/Nashit/Desktop/hnet.com-image.ico")
#declare variable
gusername=StringVar()
gpass=StringVar()

#functional Work





def profile(idfirstname,idlastname,idemail,idusername,Username,idpassword,idcoin):
    def readdata():
        with open("data.txt",'r')as read:
            wordallinfo=[]
            for i in read.readlines():
                word=i.strip().split(" ")
                wordallinfo+=word
        return wordallinfo

    def getallinfo():
        return idemail

    profile = Tk()
    profile.title("MyApp")
    profile.geometry("500x600")
    profile.config(bg="white")

    profile.iconbitmap(r"c:/Users/Nashit/Desktop/hnet.com-image.ico")






    hudaitan = Label(profile, bg="#45a9e7",text="___________________________________________________________________________________________________",fg="#45a9e7").place(x=0, y=41)
    apptitle1 = Label(profile, text=" ", font=("Arial", 4, "bold"), bg="#45a9e7").pack(fill=BOTH)
    apptitle = Label(profile, text="MyApp", font=("Arial", 20, "bold"), bg="#45a9e7").pack(fill=BOTH)
    idname = Label(profile, text=f"{idfirstname} {idlastname}", bg="white", font=("times", 19, "bold"),fg="#0072A0").place(x=55, y=63)
    newusername=idusername
    idnameforupdate=idusername
    idusername = Label(profile, text=f"Username: {idusername}", bg="white", font=("times", 10, "bold"),fg="#45a9e7").place(x=55, y=92)
    newmail=idemail
    idemail = Label(profile, text=f"Email: {idemail}", bg="white", fg="#45a9e7", font=("times", 10, "bold")).place(x=55,y=108)
    id = Label(profile, text=f"{idfirstname[0]}", fg="white", bg="#45a9e7", font=("Arial", 14, "bold"), width=3, height=2).place(x=10,y=74)
    logoutbtn = Button(profile, text="Log Out", width=15, height=2, bg="brown", bd=0, fg="white",font=("times", 10, 'bold'), command=profile.quit).place(x=350, y=83)
    secondback = Label(profile, width=100, height=50, bg="white").place(x=0, y=138)

    backcolor = Label(profile, text="", bd=1, bg="#E1F6FF", width=34, height=15).place(x=6, y=140)
    backcolor2 = Label(profile, text="", bd=1, bg="#E1F6FF", width=34, height=31).place(x=250, y=140)
    backcolor3 = Label(profile, text="", bd=1, bg="#E1F6FF", width=34, height=15).place(x=6, y=370)
    def coinbalance():
        # def get(idcoin):
        #     return idcoin

        idcoinval = idcoin
        balance = Tk()
        balance.geometry("300x200")
        balance.title("MyApp")
        update=readdata()

        balance.iconbitmap(r"c:/Users/Nashit/Desktop/hnet.com-image.ico")
        newcoininfo=0
        for i in range(len(update)//6):
            if update[3+(i*6)]==idnameforupdate:
                newcoininfo=update[5+(6*i)]
                break

        new=newcoininfo

        balancetitle = Label(balance, text="Coin Amount", font=("arial", 15, "bold")).place(x=86, y=30)
        backammount = Label(balance, width=30, height=6, bg="#45a9e7").place(x=42, y=68)
        ammount = Label(balance, text=f"{new}", font=("times", 50, "bold"), bg="#45a9e7").place(x=115, y=75)
        balance.mainloop()


    checkbalance = Label(profile, text="Check Coin", bg="#E1F6FF", font=("times", 20, "bold"), fg="black").place(x=50,y=222)
    checkbalancesubt = Label(profile, text="To check your coin please click on \nthe 'Send Request' Button",bg="#E1F6FF", font=("times", 10, "normal"), fg="black").place(x=25, y=262)
    sendreq1 = Button(profile, text="Send Request", bg="#45a9e7", bd=0, font=("times", 14, "bold"), fg="white",command=coinbalance).place(x=54, y=310)
    service01 = Label(profile, text="1", bg="#c4c4c3", font=("Arial", 14, "bold"), width=3, height=2).place(x=100,y=170)




    rusername = StringVar()
    countcoinsend = StringVar()

    def action():
        def cointransfermail(email1,coin1,firstnamer,lastnamer,firstnames,lastname,coinsend):
            import smtplib
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("nashitautomail27@gmail.com", "automailforproject")
            server.sendmail("nashitautomail27@gmail.com", email1, "Subject: Coin Transfer Confirmation\n"
                                                                 f"Hi {firstnames} {lastnames}!\n{coinsend} coins are succesfully transfferd to {firstnamer} {lastnamer}\n"
                                                                 f"Amount of Coins: {coin1}\n\n"
                                                                 f"Thanks for being with us! For any queries click on the link: https://www.facebook.com/NashitAkhanda\n"
                                                                 f"Have fun with MyApp! Bye!\n\n"
                                                                 f"From\n"
                                                                 f"MyApp Team")
            server.quit()
        def cointransfer2(emailt,coin2,firstnamer,lastnamer,firstnames,lastnames,coinsend):
            import smtplib
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("nashitautomail27@gmail.com", "automailforproject")
            server.sendmail("nashitautomail27@gmail.com", emailt, "Subject: Coin Transfer Confirmation\n"
                                                                  f"Hi {firstnamer} {lastnamer}!\nYour have got {coinsend} coins from {firstnames} {lastnames}\n"
                                                                  f"Amount of coins: {coin2}\n\n"
                                                                  f"Thanks for being with us! For any queries click on the link: https://www.facebook.com/NashitAkhanda\n"
                                                                  f"Have fun with MyApp! Bye!\n\n"
                                                                  f"From\n"
                                                                  f"MyApp Team")
            server.quit()



        flag=0
        sendto = simpledialog.askstring("Coin Transfer", "Receiver's Username")
        coinamount = simpledialog.askstring("Coin Transfer", "Amount of coins")
        confirmpassword=simpledialog.askstring("Coin Transfer", "Your Password")
        alldata1=readdata()
        count=0
        count1=0
        count2=0
        for i in range(len(alldata1)//6):
            if alldata1[4+(i*6)]==confirmpassword:
                count+=1
                if int(alldata1[5+(6*i)])>=int(coinamount):
                    count1+=1
                    val=int(alldata1[5+(6*i)])-int(coinamount)
                    alldata1[5 + (6 * i)]=str(val)
                    senderpos=i
                    coin1 = alldata1[5 + (6 * senderpos)]
                    email1 = alldata1[2 + (6 * senderpos)]
                    firstnames = alldata1[0 + (senderpos * 6)]
                    lastnames = alldata1[1 + (senderpos * 6)]

                    for j in range(len(alldata1) // 6):
                        if alldata1[3+(j*6)]==sendto:
                            senval=int(alldata1[5+(6*j)])+int(coinamount)
                            alldata1[5 + (6 * j)]=str(senval)
                            recieverpos=j
                            tkinter.messagebox.showinfo("MyApp","Coins are Successfully Sent")
                            firstnamer = alldata1[0 + (recieverpos * 6)]
                            lastnamer = alldata1[1 + (recieverpos * 6)]
                            coin2 = alldata1[5 + (recieverpos * 6)]
                            emailt = alldata1[2 + (recieverpos * 6)]
                            coinsend=coinamount
                            cointransfermail(email1,coin1,firstnamer,lastnamer,firstnames,lastnames,coinsend)
                            cointransfer2(emailt, coin2, firstnamer, lastnamer, firstnames, lastnames, coinsend)

                            count2+=1

                            break
                        else:
                            count2=0
                else:
                    count1=0
            else:
                count=0

        # if count2==0:
            # tkinter.messagebox.showinfo("MyApp","Invalid Recipant")
        if count1==0:
            tkinter.messagebox.showinfo("MyApp","Sorry, You don't have sufficient Coin")
        # elif count==0:
        #     tkinter.messagebox.showinfo("MyApp","Invalid Password")


        with open("data.txt",'w')as updatedata:
            for i in range(len(alldata1)):
                updatedata.write(alldata1[i]+" ")

    SendCoin = Label(profile, text="Transfer Coin", bg="#E1F6FF", font=("times", 20, "bold"), fg="black").place(x=290,y=338)
    UsernameTo = Label(profile, text="To send coins please click\n on the 'Send Coin' Button", bg="#E1F6FF", font=("times", 14, "normal"),fg="black").place(x=260, y=375)
    # receiverID = Entry(profile, textvar=rusername, width=20, font=10, bg="#DCDCDC", bd=0).place(x=260, y=353)
    # Coinammount = Label(profile, text="Coin Amount :", bg="#E1F6FF", font=("times", 12, "normal"), fg="black").place( x=260, y=388)
    # coincount = Entry(profile, textvar=countcoinsend, width=20, font=10, bg="#DCDCDC", bd=0).place(x=260, y=410)
    ActionButton = Button(profile, text="Send Coin", bg="#45a9e7", bd=0, font=("times", 14, "bold"), fg="white",command=action).place(x=313, y=440)
    service02 = Label(profile, text="3", bg="#c4c4c3", font=("Arial", 14, "bold"), width=3, height=2).place(x=350,y=280)

    def profileDetail():

        mydetail = Tk()
        mydetail.geometry("500x300")
        mydetail.title("MyApp / My Profile")

        mydetail.iconbitmap(r"c:/Users/Nashit/Desktop/hnet.com-image.ico")

        def change():
            password=simpledialog.askstring("Change Password","Write new password")
            # print(password)
            with open("data.txt",'r')as data:
                allinfo=[]
                for word in data.readlines():
                    words = word.strip().split(" ")
                    allinfo += words

            for j in range(len(allinfo)):
                if allinfo[j]== idpassword:
                    allinfo[j]= password
                    # print(allinfo[j])
                    break
            # print(allinfo)
            with open("data.txt","w")as datawrite:
                for i in range(len(allinfo)):
                    datawrite.write(allinfo[i]+" ")
        def finddata():
            alldata=readdata()
            password=0
            for i in range(len(alldata)//6):
                if alldata[3+(i*6)]==newusername:
                    password=alldata[4+(i*6)]
                    break
            return password
        # exit()

        passwordupdate=finddata()

        hudaitan = Label(mydetail, bg="#45a9e7",
                         text="___________________________________________________________________________________________________",
                         fg="#45a9e7").place(x=0, y=34)
        apptitle1 = Label(mydetail, text=" ", font=("Arial", 2, "bold"), bg="#45a9e7").pack(fill=BOTH)
        apptitle = Label(mydetail, text="MyApp", font=("Arial", 20, "bold"), bg="#45a9e7").pack(fill=BOTH)
        id = Label(mydetail, text=f"{idfirstname[0]}", fg="white", bg="#45a9e7", font=("Arial", 40, "bold"), width=4,
                   height=3).place(x=20, y=74)
        name = Label(mydetail, text="Name", font=("times", 13, "bold"), fg="black").place(x=160, y=72)
        namefull = Label(mydetail, text=f"{idfirstname} {idlastname}", font=("times", 20, "bold"), fg="black").place(x=160,y=90)
        Password = Label(mydetail, text="Password", font=("times", 13, "bold"), fg="black").place(x=160, y=123)
        PasswordFull = Label(mydetail, text=f"{passwordupdate}", font=("times", 20, "bold"), fg="black").place(x=160, y=142)
        Email = Label(mydetail, text="Email", font=("times", 13, "bold"), fg="black").place(x=160, y=176)
        Emailfull = Label(mydetail, text=f"{newmail}", font=("times", 17, "bold"), fg="black").place(x=160, y=195)
        Changebutton = Button(mydetail, text="Change Password", width=15, height=2, bg="#45a9e7", bd=0, fg="white",
                              font=("times", 10, 'bold'),command=change).place(x=260, y=233)

        mydetail.mainloop()

    myaccount = Label(profile, text="Profile Settings", bg="#E1F6FF", font=("times", 20, "bold"), fg="black").place(x=40,y=454)
    myaccountsubt = Label(profile, text="To see your profile please click on \nthe 'My Profile' Button", bg="#E1F6FF",font=("times", 10, "normal"), fg="black").place(x=25, y=492)
    seeabout = Button(profile, text="My Profile", bg="#45a9e7", bd=0, font=("times", 14, "bold"), fg="white",command=profileDetail).place(x=70, y=537)
    service03 = Label(profile, text="2", bg="#c4c4c3", font=("Arial", 14, "bold"), width=3, height=2).place(x=100,y=403)

    profile.mainloop()


def loggedin():
    flag=0
    Uname=gusername.get()
    PassW=gpass.get()
    # print(PassW)
    with open("data.txt", mode="r") as s_text:
        data_all = []
        for words in s_text.readlines():
            word = words.strip().split(" ")
            data_all += word
    print(data_all)
    datarange=len(data_all)//6
    position=0
    for j in range(datarange):
        if data_all[3+(j*6)]==Uname:
            if data_all[4+(j*6)]==PassW:
                flag=1
                position=j
                break
    if flag==1:
        print("Yes")
        idfirstname=data_all[0+(position*6)]
        idlastname=data_all[1+(position*6)]
        idemail=data_all[2+(position*6)]
        idusername=data_all[3+(position*6)]
        Username=data_all[3+(position*6)]
        idpassword=data_all[4+(position*6)]
        idcoin=data_all[5+(position*6)]


        profile(idfirstname,idlastname,idemail,idusername,Username,idpassword,idcoin)
        # get(idcoin)

    else:
        tkinter.messagebox.showinfo("MyApp","Invalid Username or Password")



logoPic=Image.open("C:/Users/Nashit/Desktop/1713924.png")
resizelogoPic=logoPic.resize((100,100),Image.ANTIALIAS)
newpic=ImageTk.PhotoImage(resizelogoPic)
photolebel=Label(login,image=newpic)
photolebel.place(x=173,y=90)
login.title("MyApp")


logtitle1=Label(login,text="MyApp",font=("Helvetica",30,"bold"),fg="#45a9e7").place(x=155,y=190)
logtitle2=Label(login,text="Login here using your Username and Password",font=("times",12),fg="#7eb5d6").place(x=80,y=240)
hudaitan=Label(login,text="_____________________________________________________________________________",fg="#d4d4d3").place(x=26,y=262)


giveUsername=Label(login,text="Username    :",font=("mattiface",14,"bold"),fg="#90908d").place(x=28,y=300)
giveUsernametry=Entry(login,textvar=gusername,width=23,font=14,bg="#DCDCDC",bd=0).place(x=162,y=303)

givePassword=Label(login,text="Password    :",font=("mattiface",14,"bold"),fg="#90908d").place(x=28,y=350)
givePasswordetry=Entry(login,textvar=gpass,width=23,font=14,bg="#DCDCDC",bd=0).place(x=162,y=353)
loginbtn=Button(login,text="Login",bg="#45a9e7",fg="white",width=30,bd=0,height=2,command=loggedin).place(x=115,y=440)
sorttiltle=Label(login,text=" MyApp / Login",fg="#90908d").grid(row=1,column=1)

# insidebgcolor=Label(login,bg="#F2F3F4",width=80,height=23).place(x=62,y=110)


login.mainloop()
