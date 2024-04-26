import tkinter as tk

root = tk.Tk()
root.title("Εργασία")

canvas = tk.Canvas (root, width= 500, height= 500)
canvas.grid ( row = 0, column =0, columnspan = 3)


def number():
    canvas.delete('all')
    


def clear():
    canvas.delete('all')


button1 = tk.Button (root, text = "NUMBER", bg = 'green', font = ('Arial bold', 20), command = number)
button1.grid (row =1, column =0)

button2 = tk.Button (root, text = "CLEAR", bg = 'yellow', font = ('Arial bold', 20), command = clear)
button2.grid (row =1, column =1)

button3 = tk.Button (root, text = "EXIT", bg = 'red', font = ('Arial bold', 20), command = root.destroy)
button3.grid (row =1, column =2)

label = tk.Label (root, text = 'NUMBER = ', font = ('Arial bold,', 20), bg = 'white')
label.grid(row = 2, column = 0, columnspan =3)





root.mainloop()