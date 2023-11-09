from tkinter import *

root = Tk()
entry = Entry(root, width=35, borderwidth=5)
entry.bind("<Key>", lambda a: "break")
entry.grid(row = 0, column = 0, columnspan=3)
global operation
operation = None


def number_clicked(number):
    entry.insert(END, number)
        

def create_number_button(number, row, col):
    new_button = Button(root, text = str(number), command=lambda: number_clicked(number), padx=40, pady=20)
    new_button.grid(row = row, column = col)
    
def clear():
    entry.delete(0, 'end')
    
    
def action(function):
    val = entry.get()
    if val == None:
        return
    global f_num
    f_num = float(entry.get())
    global operation
    operation = function
    clear()
    
def equals():
    second_num = float(entry.get())
    if operation == None or second_num == None:
        return
    clear()
    entry.insert(0, operation(f_num, second_num))
   
for i in range(0, 10):
    if i == 0:
        create_number_button(0, row = 4, col = 0)
        continue
    create_number_button(i, row = 3 - ((i - 1) // 3), col = (i - 1) % 3)
    
clear_button = Button(root, text = "AC", command = clear, padx = 82.5, pady = 20)
clear_button.grid(row = 4, column = 1, columnspan = 2)

add_button = Button(root, text = "+", command=lambda: action(lambda x, y: x + y), padx=40, pady=20)
add_button.grid(row = 5, column = 0)

subtract_button = Button(root, text="-", command = lambda: action(lambda x, y: x - y), padx = 40, pady = 20)
subtract_button.grid(row=5, column = 1)

mult_button = Button(root, text = "x", command=lambda: action(lambda x, y: x * y), padx = 40, pady = 20)
mult_button.grid(row=6, column=0)

divide_button = Button(root, text="/", command = lambda: action(lambda x, y: x / y), padx = 40, pady = 20)
divide_button.grid(row=6, column = 1)

eq_button = Button(root, text="=", command=equals, padx = 40, pady = 20)
eq_button.grid(row=6, column = 2)


root.mainloop()