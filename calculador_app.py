from tkinter import *

main = Tk()
main.title('Simple Calculator')

e = Entry(main, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

e.insert(0, '')

def button_add():
    return

# Define buttons

button_1 = Button(main, text='1', padx=40, pady=20, command=button_add)
button_2 = Button(main, text='2', padx=40, pady=20, command=button_add)
button_3 = Button(main, text='3', padx=40, pady=20, command=button_add)
button_4 = Button(main, text='4', padx=40, pady=20, command=button_add)
button_5 = Button(main, text='5', padx=40, pady=20, command=button_add)
button_6 = Button(main, text='6', padx=40, pady=20, command=button_add)
button_7 = Button(main, text='7', padx=40, pady=20, command=button_add)
button_8 = Button(main, text='8', padx=40, pady=20, command=button_add)
button_9 = Button(main, text='9', padx=40, pady=20, command=button_add)
button_0 = Button(main, text='0', padx=40, pady=20, command=button_add)

#put the buttons on the screen
button_1.grid(row=,column=)
button_2.grid(row=,column=)
button_3.grid(row=,column=)

button_4.grid(row=,column=)
button_5.grid(row=,column=)
button_6.grid(row=,column=)

button_7.grid(row=,column=)
button_8.grid(row=,column=)
button_9.grid(row=,column=)

button_0.grid(row=,column=)
main.mainloop()

