import tkinter as tk        # tkinter - gui library for fun stuff
from time import strftime   # strftime - can modify time date as needed

root = tk.Tk()
root.title = "Digital Clock"


def time():
    string = strftime("%I:%M:%S %p \n %D")
    label.config(text=string)
    label.after(1000, time)


label = tk.Label(root, font=('calibri', 50, 'bold'),
                 background='yellow', foreground='black')
label.pack(anchor='center')

time()
root.mainloop()
