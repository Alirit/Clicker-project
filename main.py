from tkinter import *
from threading import Thread

#______________________________________________________________
#Window preferences

window = Tk()
window.title("Новое окно")
window.geometry('400x500')

score = 0

first_upgrade = 0
first_upgrade_price = 20

second_upgrade = 0
second_upgrade_price = 2000


#______________________________________________________________
#Empty labels
empty_lbl_0 = Label(window, text = " ")
empty_lbl_0.grid(column = 0, row = 1)

empty_lbl_1 = Label(window, text = " ")
empty_lbl_1.grid(column = 0, row = 2)

empty_lbl_2 = Label(window, text = " ")
empty_lbl_2.grid(column = 0, row = 3)

empty_lbl_3 = Label(window, text = " ")
empty_lbl_3.grid(column = 0, row = 5)

empty_lbl_4 = Label(window, text = " ")
empty_lbl_4.grid(column = 0, row = 8)


#______________________________________________________________
#Function increasing score
def clicked():
  global score, first_upgrade 
  score =score + 1 + int(first_upgrade*1.5) + int(second_upgrade*10)
  lbl.configure(text="Score - " + str(score))
  
#Function increasing level of first upgrade
def Upgrade_1():
  global first_upgrade, score, first_upgrade_price
  if score >= first_upgrade_price:
    score -= first_upgrade_price
    first_upgrade +=1
    first_upgrade_price = int(first_upgrade_price*2.2)
    lbl_upgrade_1.configure(text = "Upgrade level - " + str(first_upgrade))
    lbl.configure(text="Score - " + str(score))
    lbl_up1_price.configure(text = "Price - " + str(first_upgrade_price))
    btn.configure(text = "score + " + str(1 + int(first_upgrade*1.5) +
                                          int(second_upgrade*10)))

def Upgrade_2():
  global score, second_upgrade, second_upgrade_price
  if score>=second_upgrade_price:
    score -= second_upgrade_price
    second_upgrade +=1
    second_upgrade_price = int(second_upgrade_price*5.8)
    lbl_up_2.configure(text = "Upgrade level - " + str(second_upgrade))
    lbl.configure(text = "Score - " + str(score))
    lbl_up2_price.configure(text = "Price - " + str(second_upgrade_price))
    btn.configure(text = "score + " + str(1 + int(first_upgrade*1.5) + 
                                         int(second_upgrade*10)))

#______________________________________________________________
# Label

#Score label
lbl = Label(window,
            text="Score - " + str(score),
            font=("Times New Roman", 20))

lbl.grid(column=0,row=0)

#Label of 1st upgrade's level
lbl_upgrade_1 = Label(window,
                     text = "Upgrade level - " + str(first_upgrade),
                     font = ("Times New Roman", 12))
lbl_upgrade_1.grid(column = 1, row = 6)

#Label of 1st upgrade's price
lbl_up1_price = Label(window,
                     text = "Price - " + str(first_upgrade_price),
                     font = ("Times New Roman", 12))
lbl_up1_price.grid(column = 0, row = 7)

#Label of 2nd upgrade's level
lbl_up_2 = Label(window,
                text = "Upgrade level - " + str(second_upgrade),
                font = ("Times New Roman", 12))
lbl_up_2.grid(column = 1, row = 9)

#Label of 2nd upgrade's price
lbl_up2_price = Label(window,
                     text = "Price - " + str(second_upgrade_price),
                     font = ("Times New Roman", 12))
lbl_up2_price.grid(column = 0, row = 10)


#______________________________________________________________
#Button, increasing score
btn=Button(window,
           text="score + 1",
           font=("Times New Roman", 16),
           command=clicked)

btn.grid(column=0, row=4)

#Button, 1st upgrade
btn_upgrade_1 = Button(window,
                      text = "1st upgrade - " + str(first_upgrade*2+1),
                      font = ("Times New Roman", 12),
                      command=Upgrade_1)
btn_upgrade_1.grid(column = 0, row = 6)

#Button, 2nd upgrade
btn_up_2 = Button(window,
                 text = "2nd upgrade - " + str(second_upgrade*20),
                 font = ("Times New Roman", 12),
                 command = Upgrade_2)
btn_up_2.grid(column = 0, row = 9)

window.mainloop()
