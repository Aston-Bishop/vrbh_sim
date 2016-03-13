from Tkinter import *
import ttk
import Globals

def exit():
    root.destroy()

def start():
    Globals.item_num = int(item_cmb.get())
    Globals.time_num = int(time_cmb.get())
    Globals.matrix_size = int(size_cmb.get())

    root.destroy()
    import Simulation

root = Tk()
#root.geometry("450x450+300+300")
root.title("Configuration")

item_lbl = Label(text="Number of Items to Generate:").grid(row=0, column=0, sticky =W)

item_txt = StringVar()
item_cmb = ttk.Combobox(root, textvariable = item_txt)
item_cmb.config(values = ("3","4","5","6","7","8","9"))
item_cmb.set("3")
item_cmb.grid(row=0, column=1, sticky =W)

time_lbl = Label(text="How long should the simulation run for (Seconds):").grid(row=1, column=0, sticky =W)

time_txt = StringVar()
time_cmb = ttk.Combobox(root, textvariable = time_txt)
time_cmb.config(values = ("15","30","45","60"))
time_cmb.set("15")
time_cmb.grid(row=1, column=1, sticky =W)

size_lbl = Label(text="Size of the matrix (Nodes for Height and Width):").grid(row=2, column=0, sticky =W)

size_txt = StringVar()
size_cmb = ttk.Combobox(root, textvariable = size_txt)
size_cmb.config(values = ("10","20","30","40","50"))
size_cmb.set("10")
size_cmb.grid(row=2, column=1, sticky =W)

exit_but = Button(text="Exit", command = exit).grid(row=3, column=0, sticky=N+S+E+W)

start_but = Button(text="Start", command = start).grid(row=3, column=1, sticky=N+S+E+W)

root.mainloop()

