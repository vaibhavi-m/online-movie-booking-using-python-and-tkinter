import tkinter
from tkinter import messagebox
from sys import *

x = 10
Booked_seat = 0
prize_of_ticket = 200
Row = 12
Seats = 12
Total_seat = Row * Seats
Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]

a = open('file10.txt', 'a')

print('\nWelcome to Online movie ticket booking system. Please choose an option:')

box = tkinter.Tk()
box.withdraw()

class chart:

    @staticmethod
    def chart_maker():
        seats_chart = {}
        for i in range(Row):
            seats_in_row = {}
            for j in range(Seats):
                seats_in_row[str(j + 1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart


class_call = chart
table_of_chart = class_call.chart_maker()


def repeat():
    global x
    global Booked_seat
    print("PLEASE ENTER THE MOVIE YOU WANT TO WATCH\n 1.SPIDERMAN\n 2.ATRANGI RE\n 3.BLACKLIGHT\n 4.PUSHPA")
    select=input()
    while x != 0:
        #print("PLEASE ENTER THE MOVIE YOU WANT TO WATCH")
        #select=input("\n 1.SPIDERMAN\n 2.ATRANGI RE\n 3.BLACKLIGHT\n 4.PUSHPA")
        print('\n1 for Show the seats \n2 for Buy a Ticket \n3 for Statistics ',
              '\n4 for Show booked Tickets User Info \n0 for Exit')
        x = int(input('Select Option - '))
        if x == 1:
            print(Seats)
            count_num = 0
            for num in table_of_chart.keys():
                if int(list(table_of_chart.keys())[count_num]) < 9:
                    print(int(num) + 1, end='  ')
                else:
                    print(int(num) + 1, end=' ')
                count_key = 0
                for no in table_of_chart[num].values():
                    if int(list(table_of_chart[num].keys())[count_key]) <= 10:
                        print(no, end='  ')
                    else:
                        print(no, end='  ')
                    count_key += 1
                count_num += 1
                print()
            print('Vacant Seats = ', Total_seat - Booked_seat)
            print()
        elif x == 2:
            Row_number = int(input('Enter Row Number - \n'))
            Column_number = int(input('Enter Column Number - \n'))
            if Row_number in range(1, Row + 1) and Column_number in range(1, Seats + 1):
                if table_of_chart[str(Row_number - 1)][str(Column_number)] == 'S':
                    confirm = messagebox.askyesno("Do you wish to book a ticket?", "Do you wish to book a ticket?")
                    person_detail = {}
                    if confirm:
                        person_detail['Name'] = input('Enter Name - ')
                        person_detail['Gender'] = input('Enter Gender - ')
                        person_detail['Age'] = input('Enter Age - ')

                        not_booked = True
                        while not_booked:
                            person_detail['Phone_No'] = input('Enter Phone number - ')
                            if len(person_detail['Phone_No']) == 10:
                                table_of_chart[str(Row_number - 1)][str(Column_number)] = 'B'
                                Booked_seat += 1
                                Booked_ticket_Person[Row_number - 1][Column_number - 1] = person_detail
                                messagebox.showinfo("CONGRATULATIONS", "Booked successfully")
                                import sys

                                original_stdout = sys.stdout
                                with open('temp-file.txt', 'w') as f:
                                    f.write("\n")
                                    sys.stdout = f
                                    print('Number of purchased Ticket - ', Booked_seat)
                                    print('price - ', Booked_seat * prize_of_ticket)
                                    sys.stdout = original_stdout
                                not_booked = False
                            else:
                                messagebox.showerror("ERROR", "Invalid Phone number")
                                continue
                else:
                    messagebox.showinfo("INFO", "This seat is already booked")
            else:
                messagebox.showerror("Error", "INVALID INPUT")

        elif x == 3:
            print('Number of purchased Ticket - ', Booked_seat)
            print('price - ', Booked_seat * prize_of_ticket)

        elif x == 4:
            Enter_row = int(input('Enter Row number - \n'))
            Enter_column = int(input('Enter column number-\n'))
            if Enter_row in range(1, Row + 1) and Enter_column in range(1, Seats + 1):
                if table_of_chart[str(Enter_row - 1)][str(Enter_column)] == 'B':
                    person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]

                    import tkinter as tk

                    root = tk.Toplevel()
                    canvas = tk.Canvas(root, width=700, height=325)
                    canvas.pack()
                    img = tk.PhotoImage(file="Movie-ticket-Templates-9_1_LI.ppm")
                    canvas.create_image(20, 20, anchor=tk.NW, image=img)
                    text = canvas.create_text((140, 150), text=".", font=("Comic Sans MS", 1), fill='black')
                    text = canvas.create_text((140, 150), text="Name   :    " + person["Name"],
                                              font=("Comic Sans MS", 10),
                                              fill='black')
                    text = canvas.create_text((165, 165), text="Age    :    " + person["Age"],
                                              font=("Comic Sans MS", 10),
                                              fill='black')
                    text = canvas.create_text((200, 180), text="Gender :    " + person["Gender"],
                                              font=("Comic Sans MS", 10), fill='black')
                    text = canvas.create_text((225, 195), text="Contact:    " + person["Phone_No"],
                                              font=("Comic Sans MS", 10), fill='black')
                    text=canvas.create_text((245,210),text="Movie:"+select,font=("Comic Sans MS", 10),fill='black')
                    c = messagebox.askyesno("Ask", "Do you wanna continue?")
                    if c:
                        print(repeat())
                    else:
                        print("\nStopping program...")
                        f = open("temp-file.txt", 'r')
                        a.write(f.read())
                        a.write("\n           * Session Ended *           ")
                        exit()
                    root.mainloop()

                else:
                    messagebox.showinfo("INFO", "VACANT SEAT")
            else:
                messagebox.showerror("error", "Invalid input")
        elif x != 0:
            messagebox.showerror("error", "Invalid input")
        else:
            print("\nStopping program...")
            f = open("temp-file.txt", 'r')
            a.write(f.read())
            a.write("\n           * Session Ended *           ")
            exit()

    box.mainloop()


print(repeat())