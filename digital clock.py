import tkinter as tk
from  time import strftime

root = tk.Tk()
root.title("Digital clock")

def time():
    string = strftime("%H:%M%S %P \n %D ")
    label.config(text = string )
    label.after(1000,time)  # it help to update time functions every second and show current date and time

label = tk.label (root, front = ('calibri', 50, 'bold' ), backround ='yellow', foreground = 'black')
label.pack(archar = 'center')

time()

root.mainloop()