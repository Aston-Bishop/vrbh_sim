from Tkinter import *
import ttk
import Globals

root = Tk()
#root.geometry("450x450+300+300")
root.title("Items Found")

def exit():
    root.destroy()

Label(text="Items Found:").grid(row=0, column=0, sticky =W)

count=1

for item in Globals.item_names:
    Label(text=Globals.item_names[count-1]).grid(row=count, column=0, sticky =W)

    count = count+1

exit_but = Button(text="Exit", command = exit).grid(row=count+1, column=0, sticky=N+S+E+W)

root.mainloop()