from msilib.schema import ComboBox
from cgitb import text
from tkinter import * #Imports Tkinter
import sys #Imports sys, used to end the program later
from functools import partial
from tkinter import ttk
#from PIL import ImageTk, Image

def validatelogin(username,password):
    global entereduser
    global enteredpassword
    entereduser=("USERNAME ",username.get())
    print(entereduser)
    enteredpassword=print("PASSWORD ",password.get())
    print(enteredpassword)

root=Tk() #Declares root as the tkinter main window
top = Toplevel() #Creates the toplevel window

top.title('LOGIN')
root.title('BOOK YOUR SHOW! ')


labeluser=Label(top,text="USERNAME").place(x=40,y=60)
username=StringVar()
entry1 = Entry(top,textvariable=username).place(x=110,y=60) #Username entry
Label_pass=Label(top,text="PASSWORD").place(x=40,y=100)
password=StringVar()
entry2 = Entry(top,textvariable=password,show='*').place(x=110,y=100) #Password entry.
#shows password as *

validatelogin=partial(validatelogin,username,password)

#login button
button1 = Button(top, text="Login", command=lambda:command1()).place(x=40,y=130)
#Cancel button
button2 = Button(top, text="Cancel", command=lambda:command2()).place(x=90,y=130)
label1 = Label(root, text="WELCOME! ENTER THE NUMBER OF TICKETS. " ).place(x=10,y=20)
m1button = Button(root, text="MOVIE 1", command=lambda:matr1()).place(x=90,y=150)
m1button = Button(root, text="MOVIE 2", command=lambda:matr1()).place(x=190,y=150)
m1button = Button(root, text="MOVIE 3", command=lambda:matr1()).place(x=290,y=150)

#for ticket count validation.
def validatetickets(ticket_number):
    enteredtickets=("no. of tickets: ", ticket_number.get())
    enteredtickets=int(enteredtickets)
    print(enteredtickets)#for checking purpose. Console print
    return
            
def command1():
    print("USERNAME ",username.get())
    print("PASSWORD ",password.get())
    root.deiconify() #Unhides the root window
    top.destroy() #Removes the toplevel window

ticket_number=IntVar() #integer variable. default value is 0
#IntVar() is used to declare the textvariable name. 

#Entry to get number of tickets
entry=Entry(root,width=25,textvariable=ticket_number).place(x=40,y=50)

validateticket = partial(validatetickets,ticket_number)
    
#button to get the value of number of tickets
button2=Button(root, text="OK", command=lambda:ticketscommmand()).place(x=150,y=100)


tickets=ticket_number.get()

#selecting seats
def matr1():
    global top2
    top2=Toplevel()
    top2.withdraw()
    top2.deiconify()
    #button to go to next page
    next_btn=Button(top2,text="Next",command=lambda:confirm()).place(x=400,y=350)
    #to get 144 seats in a matrix in the form of buttons
    for row in range(12):
        for col in range(12):
            btn=Button(top2, text='(%d, %d)'% (col, row),bg='white')
            #command to change button colour when selected for easy differentiation
            btn['command']=lambda b=btn: b.config(bg='black')
            btn.grid(row=row, column=col)


#next window to confirm the seats
def confirm():
    global top3
    top3=Toplevel()
    top3.deiconify()
    label_confirm=Label(top3,text="Do you want to confirm?").place(x=30,y=20)
    #yes button takes us to the next window which is details page 
    b_yes=Button(top3,text="Yes",command=lambda: details()).place(x=50,y=40)
    #no button exits the system
    b_no=Button(top3,text="No",command=lambda: command2()).place(x=90,y=40)

#details of user
def details():
    global name
    global phone
    global card
    global passw
    top4=Toplevel()
    top2.destroy()
    top3.destroy()
    top4.title('Deatils Page')
    label_d2=Label(top4,text="Enter your details.").place(x=10,y=10)
    label_d2=Label(top4,text="Name:").place(x=10,y=40)
    name=StringVar()
    #entry widget for name
    entry_d2=Entry(top4,textvariable=name).place(x=60,y=40)
    label_d3=Label(top4,text="Phone number:").place(x=10,y=60)
    phone=StringVar()
    #entry widget for phone number
    entry_d3=Entry(top4,textvariable=phone).place(x=100,y=60)
    payment=Label(top4,text="payment:").place(x=10,y=90)
    #combobox for payment
    pay=StringVar()
    paymentchosen= ttk.Combobox(top4,width=27, textvariable=pay)
    #adding combobox drop down list
    paymentchosen['values']=('CREDIT CARD','DEBIT CARD','NET BANKING','OTHER')
    paymentchosen.place(x=80,y=90)
    cardno=Label(top4,text="CARD NUMBER").place(x=10,y=120)
    card=IntVar()
    cardno_entry=Entry(top4,textvariable=card).place(x=120,y=120)
    Password=Label(top4,text="PASSWORD").place(x=10,y=150)
    passw=StringVar()
    pass_entry=Entry(top4,textvariable=passw).place(x=80,y=150)
    But_done=Button(top4,text="DONE",command=lambda:command_done()).place(x=50,y=200)

#to print the ticket     
def command_done():    
    top5=Toplevel()
    #a canvas is created to print the ticket
    canvas = Canvas(top5, width=700, height=300)
    canvas.pack()
    img = PhotoImage(file="Movie-ticket-Templates-9_1_LI.ppm")
    ticket=str(ticket_number.get())
    canvas.create_image(20, 20, anchor=NW, image=img)
    text = canvas.create_text((140, 150), text=".", font=("Comic Sans MS", 1), fill='black')
    text = canvas.create_text((140, 150), text="Name   :    "+ (name.get()), font=("Comic Sans MS", 15), fill='black')
    text = canvas.create_text((180, 220), text="Contact:    "+ (phone.get()), font=("Comic Sans MS", 15), fill='black')
    text = canvas.create_text((130, 175), text="tickets    :    "+(ticket), font=("Comic Sans MS", 15), fill='black')
    text = canvas.create_text((150, 198), text="booking :    "+ (passw.get), font=("Comic Sans MS", 15), fill='black')

#for checking purpose. prints the number of tickets in terminal
def ticketscommmand():
    print("tickets: ",ticket_number.get())
    print(type(tickets))  

#exit commands
def command2():
    top.destroy() #Removes the toplevel window
    root.destroy() #Removes the hidden root window
    sys.exit() #Ends the script
def command3():
    top.destroy()
    root.destroy()
    top2.destroy()
    top3.destroy()

root.withdraw() #This hides the main window, it's still present it just can't be seen or interacted with
root.mainloop() 