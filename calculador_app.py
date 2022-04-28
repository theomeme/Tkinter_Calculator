from tkinter import Tk, BOTH, messagebox
from tkinter.ttk import Frame, Button
from tkinter import *

main = Tk()
main.title('Simple Calculator')

e = Entry(main, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

e.insert(0, '')


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def function_clear():
    e.delete(0, END)

def function_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def function_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))




# Define buttons

button_1 = Button(main, text='1', padx=40, pady=20, command = lambda: button_click(1))
button_2 = Button(main, text='2', padx=40, pady=20, command= lambda: button_click(2))
button_3 = Button(main, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(main, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(main, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(main, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(main, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(main, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(main, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(main, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(main, text='+', padx=39, pady=20, command=function_add)
button_equal = Button(main, text='=', padx=91, pady=20, command=function_equal)
button_clear = Button(main, text='Clear', padx=79, pady=20, command=lambda: function_clear())




# put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
main.mainloop()
