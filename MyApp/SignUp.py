from tkinter import *
import tkinter.messagebox
# import smtplib


signup=Tk()
signup.geometry("700x500")
signup.title("Sign up")
signup.config(bg="#45a9e7")
signup.iconbitmap(r"c:/Users/Nashit/Desktop/hnet.com-image.ico")
#windowTitle:

wtitle1=Label(signup,text="MyApp",font=("Helvetica",30,"bold"),fg="#F2F3F4",bg="#45a9e7").place(x=280,y=20)
wtitle2=Label(signup,text="Sign Up for a New Account",font=("times",12),fg="#DBE9F4",bg="#45a9e7").place(x=260,y=70)
insidebgcolor=Label(signup,bg="#F2F3F4",width=80,height=23).place(x=62,y=110)


#variable name

fn=StringVar()
ln=StringVar()
emad=StringVar()
uname=StringVar()
pswd=StringVar()
cpswd=StringVar()


#functional Work

def confirmationMail(email,first,last,coin):
    # import smtplib
    import smtplib
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("nashitautomail27@gmail.com", "automailforproject")
    server.sendmail("nashitautomail27@gmail.com", email, "Subject:Subject: Confirmation Mail\n"
                    f"Hi {first} {last}!\nWelcome to MyApp.Your account is successfully created.\n"
                    f"You have got 20 coins as bonus for signing up!\nCoin Amount: {coin}\n\n"
                    f"Thanks for being with us! For any queries click on the link: https://www.facebook.com/NashitAkhanda\n"
                    f"Have fun with MyApp! Bye!\n\n"                    
                    f"From\n"
                    f"MyApp Team")
    server.quit()

def exeuteData():
    first=fn.get()
    last=ln.get()
    email=emad.get()
    username=uname.get()
    passward=pswd.get()
    confirmpassward=cpswd.get()
    default="@gmail.com"
    vote=0
    count=0
    for i in range(len(first)):
        if (first[i] >= 'A' and first[i] <= 'Z') or (first[i] >= 'a' and first[i] <= 'z'):
            count += 1
    if count == len(first):
        vote += 1
    count = 0
    for i in range(len(last)):
        if (last[i] >= 'A' and last <= 'Z') or (last[i] >= 'a' and last[i] <= 'z'):
            count += 1
    if count == len(last):
        vote += 1
    if default in email:
        if len(email) > len(default):
            vote += 1
    count=0
    for i in range(len(username)):
        if username[i]==" ":
            count+=1
    if count==0:
        vote+=1
    if len(passward)>=6:
        vote+=1
    count=0
    if len(passward)==len(confirmpassward):
        for i in range(len(passward)):
            if passward[i]==confirmpassward[i]:
                count+=1
    if len(passward)==count:
        vote+=1
    if vote==6:
        data=""
        coin="20"
        data+=first+" "
        data+=last+" "
        data+=email+" "
        data+=username+" "
        data+=passward+" "
        data+=coin+" "
        # print(data)


        with open("data.txt",'r') as readdata:
            wordall=""
            for word in readdata.readlines():
                words=word
                wordall+=words

            wordall+=data
        with open("data.txt",'w')as writedata:
            writedata.write(wordall)


        tkinter.messagebox.showinfo("MyApp","Sign in is successfully Done!\nYou have got 20 coins as bonus for signing up!\nWe have sent a you confirmation mail.")
        confirmationMail(email,first,last,coin)
        # exit()
        # print(wordall)


    else:
        tkinter.messagebox.showinfo("MyApp","Invalid Input. Please Try again!")




# Main Part

firstname=Label(signup,text="First Name:",font=("mattiface",14,"bold"),fg="#90908d").place(x=90,y=130)
firstnameentry=Entry(signup,textvar=fn,width=20,font=14,bg="#DCDCDC",bd=0).place(x=91,y=160)
lastname=Label(signup,text="Last Name:",font=("mattiface",14,"bold"),fg="#90908d").place(x=369,y=130)
lastnameentry=Entry(signup,textvar=ln,width=20,font=14,bg="#DCDCDC",bd=0).place(x=370,y=160)
hudaitan=Label(signup,text="________________________________________________________________________________"
                           "____________________",fg="#d4d4d3").place(x=89,y=192)
Emailad=Label(signup,text="Email Address         :",font=("mattiface",14,"bold"),fg="#90908d").place(x=90,y=225)
Emailadentry=Entry(signup,textvar=emad,width=27,font=14,bg="#DCDCDC",bd=0).place(x=292,y=225)
Username=Label(signup,text="Username                 :",font=("mattiface",14,"bold"),fg="#90908d").place(x=90,y=270)
Usernameentry=Entry(signup,textvar=uname,width=27,font=14,bg="#DCDCDC",bd=0).place(x=292,y=270)

passward=Label(signup,text="Passward                 :",font=("mattiface",14,"bold"),fg="#90908d").place(x=90,y=315)
passwardentry=Entry(signup,textvar=pswd,width=27,font=14,bg="#DCDCDC",bd=0).place(x=292,y=315)
confirmpass=Label(signup,text="Confirm Passward :",font=("mattiface",14,"bold"),fg="#90908d").place(x=90,y=360)
confirmpassentry=Entry(signup,textvar=cpswd,width=27,font=14,bg="#DCDCDC",bd=0).place(x=292,y=360)
warningpass=Label(signup,text="* minimum 6 digits",font=("arial",7,"bold"),fg="#4e4e4c").place(x=500,y=340)
signupbtn=Button(signup,text="Sign Up",bg="#45a9e7",fg="white",width=30,bd=0,height=2,command=exeuteData).place(x=250,y=405)
sorttiltle=Label(signup,text=" MyApp / Sign Up",fg="light blue",bg="#45a9e7").grid(row=1,column=1)


signup.mainloop()
