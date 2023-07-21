from tkinter import  *
from tkinter import messagebox
root = Tk()
root.title("Convertor")
root.geometry('1200x660')

num = IntVar()
lblbinary = StringVar()
lbldecimal = StringVar()
lblhexa = StringVar()
lbloctal = StringVar()

def convert():
    if num.get() == 0:
        messagebox.showerror('Error', 'You must enter a number to convert')
    else:
        lblbinary.set(str(bin(num.get())))
        lbldecimal.set(str(bin(num.get())))
        lblhexa.set(str(hex(num.get())))
        lbloctal.set(str(oct(num.get())))

def clear():
    num.set(0)
    lblhexa.set('')
    lblbinary.set('')
    lbloctal.set('')
    lbldecimal.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit ?'):
        root.destroy()

Label(root, text = "Conversion System", font = ("times new rommon", 60, "bold"), bg = 'red', fg = "grey", relief = RIDGE).pack(pady = 10)

n = Label(root, text = "Enter number", font = ("times new rommon", 25, "bold"), fg = "red")
n.place(x = 300, y = 150)

b = Label(root, text = "Binary", font = ("times new rommon", 25, "bold"), fg = "black")
b.place(x = 300, y = 230)

d = Label(root, text = "Decimal", font = ("times new rommon", 25, "bold"), fg = "black")
d.place(x = 300, y = 310)

h = Label(root, text = "HexaDecimal", font = ("times new rommon", 25, "bold"), fg = "black")
h.place(x = 300, y = 390)

o = Label(root, text = "Octal", font = ("times new rommon", 25, "bold"), fg = "black")
o.place(x = 300, y = 470)

e1 = Entry(root, font = 'arial 20', fg = 'blue', justify = CENTER, relief = GROOVE, textvariable = num)
e1.place(x = 650, y = 160)

e2 = Entry(root, font = 'arial 20', fg = 'blue', justify = CENTER, relief = GROOVE, textvariable = lblbinary)
e2.place(x = 650, y = 240)

e3 = Entry(root, font = 'arial 20', fg = 'blue', justify = CENTER, relief = GROOVE,  textvariable = lbldecimal)
e3.place(x = 650, y = 320)

e4 = Entry(root, font = 'arial 20', fg = 'blue', justify = CENTER, relief = GROOVE,  textvariable = lblhexa)
e4.place(x = 650, y = 400)

e5 = Entry(root, font = 'arial 20', fg = 'blue', justify = CENTER, relief = GROOVE,  textvariable = lbloctal)
e5.place(x = 650, y = 480)

bt1 = Button(root, text = 'Convertor', font = "arial 20 bold", fg = 'crimson', bg = 'black', command = convert)
bt1.place(x = 300, y = 580)

bt2 = Button(root, text = 'Clear', font = "arial 20 bold", fg = 'crimson', bg = 'black', command = clear)
bt2.place(x = 500, y = 580)

bt3 = Button(root, text = 'Exit', font = "arial 20 bold", fg = 'crimson', bg = 'black', command = exit)
bt3.place(x = 650, y = 580)

root.mainloop()