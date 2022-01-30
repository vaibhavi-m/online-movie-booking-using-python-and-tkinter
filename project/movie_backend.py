x = 10
Booked_seat = 0
prize_of_ticket = 200
Row =12
Seats =12
tickets=int(input("no. of tickets:"))
Total_seat = Row*Seats
Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]

class chart:

    @staticmethod
    def chart_maker():
        seats_chart = {}
        for i in range(Row):
            seats_in_row = {}
            for j in range(Seats):
                seats_in_row[str(j+1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart

class_call = chart
table_of_chart = class_call.chart_maker()

while x != 0:
    print('1 for Show the seats \n2 for Buy a Ticket \n3 for Statistics ',
          '\n4 for Show booked Tickets User Info \n0 for Exit')
    x = int(input('Select Option - '))
    if x == 1:
        print(Seats)
        count_num = 0
        for num in table_of_chart.keys():
            if int(list(table_of_chart.keys())[count_num]) < 9:
                print(int(num)+1, end='  ')
            else:
                print(int(num)+1, end=' ')
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
        for i in range(tickets):
            Row_number = int(input('Enter Row Number - \n'))
            Column_number = int(input('Enter Column Number - \n'))
            if Row_number in range(1, Row+1) and Column_number in range(1, Seats+1):
                if table_of_chart[str(Row_number-1)][str(Column_number)] == 'S':
                    confirm = input('yes for booking and no for Stop booking - ')
                    person_detail = {}
                    if confirm == 'yes':
                        person_detail['Name'] = input('Enter Name - ')
                        person_detail['Gender'] = input('Enter Gender - ')
                        person_detail['Age'] = input('Enter Age - ')
                        person_detail['Phone_No'] = input('Enter Phone number - ')
                        if len(person_detail['Phone_No'])!=10:
                           print("invalid number")
                           continue
                        #person_detail['Ticket_prize'] = prize_of_ticket
                        table_of_chart[str(Row_number-1)][str(Column_number)] = 'B'
                        Booked_seat += 1
                    else:
                        continue
                    Booked_ticket_Person[Row_number-1][Column_number-1] = person_detail
                    print('Booked Successfully')
                else:
                    print('This seat is already booked by someone')
            else:
                print()
                print('*  Invalid Input  *')
            print()

    elif x == 3:
       print('Number of purchased Ticket - ', Booked_seat)
       print('price - ', Booked_seat * prize_of_ticket)
       import sys
       original_stdout = sys.stdout
       with open('file1.txt', 'w') as f:
        sys.stdout = f
        print('Number of purchased Ticket - ', Booked_seat)
        print('price - ', Booked_seat * prize_of_ticket)
        sys.stdout = original_stdout
    elif x == 4:
        Enter_row = int(input('Enter Row number - \n'))
        Enter_column = int(input('Enter Column number - \n'))
        if Enter_row in range(1, Row+1) and Enter_column in range(1, Seats+1):
            if table_of_chart[str(Enter_row-1)][str(Enter_column)] == 'B':
                person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
                
                import tkinter as tk
                root=tk.Tk()
                canvas = tk.Canvas(root, width=700, height=300)
                canvas.pack()
                img = tk.PhotoImage(file="Movie-ticket-Templates-9_1_LI.ppm")
                canvas.create_image(20, 20, anchor=tk.NW, image=img)
                text = canvas.create_text((140, 150), text=".", font=("Comic Sans MS", 1), fill='black')
                text = canvas.create_text((140, 150), text="Name   :    "+person["Name"], font=("Comic Sans MS", 15), fill='black')
                text = canvas.create_text((130, 175), text="Age    :    "+person["Age"], font=("Comic Sans MS", 15), fill='black')
                text = canvas.create_text((150, 198), text="Gender :    "+person["Gender"], font=("Comic Sans MS", 15), fill='black')
                text = canvas.create_text((180, 220), text="Contact:    "+person["Phone_No"], font=("Comic Sans MS", 15), fill='black')
                tk.mainloop()
            else:
                print()
                print('------  Vacant seat  ------')
        else:
            print()
            print('*  Invalid Input  *')
        print()

    else:
        print()
        print('*  Invalid Input  *')
        print()