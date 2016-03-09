import sys
from Tkinter import *
import ttk
import tkFont as font
import math
import random
import time
import Node


class Interface():
    '''Displays the main menu where the user will select what they want to search
       for and how they want it to be searched '''
    def __init__(self, root):
        self.root = root
    value = "#000"
    def lables(self):
        ''' displays the labels on the main page'''
        font.nametofont('TkDefaultFont').configure(size=15)
        MyFont = font.Font(size=20)#Changes the font size
        self.labelItems = Label(root,text="Items", font=MyFont)
        self.labelItems.configure(background='white')
        self.labelItems.pack()

        self.labelType = Label(root,text="Type")
        self.labelType.configure(background='white')
        self.labelType.place(x=100,y=80)

        self.labelTime = Label(root,text="Time")
        self.labelTime.configure(background='white')
        self.labelTime.place(x=100,y=160)

        self.labelSearching = Label(root,text="Searching")
        self.labelSearching.configure(background='white')
        self.labelSearching.place(x=60,y=240)

        self.labelSorting = Label(root,text="Sorting")
        self.labelSorting.configure(background='white')
        self.labelSorting.place(x=80,y=320)

        self.lableRobotColour = Label(root,text= "Robots colour")
        self.lableRobotColour.configure(background='white')
        self.lableRobotColour.place(x=185,y=400)


    def okButton(self):
        ''' prints the values the user has choosen '''
        self.value_of_comboType = self.comboType.get()
        self.value_of_comboTime = self.comboTime.get()
        self.value_of_comboSearching = self.comboSearching.get()
        self.value_of_comboSorting = self.comboSorting.get()
        dic = { "type":self.value_of_comboType, "time":self.value_of_comboTime,
                "searching":self.value_of_comboSearching,
                "sorting":self.value_of_comboSorting,
                "colour":Interface.value
                }
        if self.value_of_comboType =="":
            print("Fill out all of the fields")
        elif self.value_of_comboTime =="":
            print("Fill out all of the fields")
        elif self.value_of_comboSearching =="":
            print("Fill out all of the fields")
        else:
            print(dic["type"],dic["time"],dic["searching"],dic["sorting"],dic["colour"])
            self.root.destroy()
            import searchAround
        
        
        
    

    def comboboxs(self):
          ''' displays the comboboxes on the main page'''
          self.comboType = ttk.Combobox(self.root)
          self.comboType.bind(self.comboType)
          self.comboType.place(x=190,y=90)
          #Place holder values atm
          self.comboType.config(values = ("a","b","c"))
          #self.text.get()

          self.textTime = StringVar()
          self.comboTime = ttk.Combobox(self.root, textvariable = self.textTime)
          self.comboTime.place(x=190,y=170)
          self.comboTime.config(values = ("a","b","c"))

          self.textSearching = StringVar()
          self.comboSearching = ttk.Combobox(self.root, textvariable = self.textSearching)
          self.comboSearching.place(x=190,y=250)
          self.comboSearching.config(values = ("a","b","c"))

          self.textSorting = StringVar()
          self.comboSorting = ttk.Combobox(self.root, textvariable = self.textSorting)
          self.comboSorting.place(x=190,y=330)
          self.comboSorting.config(values = ("a","b","c"))

    def buttons(self):
        ''' displays the button on the main page'''
        self.buttonOk = Button(self.root,text="Ok", command = self.okButton)
        self.buttonOk.place(x=600,y=600)
           
           

    def slider(self):
        ''' displays the slider on the main page'''
        self.sliderColour = Scale(root, orient =HORIZONTAL,length=200,
          width=15,sliderlength=15,
          from_=0,to=4095,
          highlightthickness=0,
          command=self.print_value)
       
        self.sliderColour.place(x=270,y=500)
        self.sliderColour.configure(background='white')
    def done(self):
        ''' close the main page and opens up a new one'''
        #root.destroy()
        #root2 = Tk()
        #root2.geometry('450x450+200+200') 

    def print_value(self,value):
        '''sets the value of the colours on the slider ''' 

        v = int(value)
        col = (hex(v)[2:])

        Interface.value = "#{}".format(col)


        canvas.itemconfig(rectangleColour, fill=Interface.value)    
           
        
class Info(Interface):
   
    
    def __init__(self, root):
        self.root = root
        
    def infomationLabel(self):
        self.labelInfo = Label(root,text="Welcome to Virtual Robot Bargain Hunt \n \n The aim of this simulation is for you to find out within a certian amount of time \n how many items you can find. \n \n After you found all the items you are able to you will be given the option \n of how you want to sort your items. ")
        self.labelInfo.configure(background='white')
        self.labelInfo.pack()
   
    def okButton1(self):
        
        self.buttonOk = Button(self.root,text="Ok",command = self.close)
        self.buttonOk.place(x=650,y=600)

    def showMeAgainButton(self):
        self.buttonShowAgain = Button(self.root,text="Don't show me again",command = self.files)
        self.buttonShowAgain.place(x=50 , y=600)
    def close(self):
        self.buttonShowAgain.place_forget()
        self.buttonOk.place_forget()
        self.labelInfo.pack_forget()
        gui.lables()
        gui.comboboxs()
        gui.buttons()
        gui.slider()
        canvas.pack(padx=10,pady=240)
    def close2(self):
         gui.lables()
         gui.comboboxs()
         gui.buttons()
         gui.slider()
         canvas.pack(padx=10,pady=240)     
    def files(self):
        f = open('H:\ALL semester 2\dont show me.txt', 'r+')
        f.write("true")
        f.close
        
        self.close()
         
   






  






root = Tk()
gui = Info(root)

root.configure(background='white')

font.nametofont('TkDefaultFont').configure(size=15)
canvas = Canvas(root, width=100, height=450,highlightthickness=0)
rectangleColour=canvas.create_rectangle(3,110,3+100,110+100,fill=Interface.value)
canvas.configure(background='white')

root.geometry('750x750')
f = open('H:\ALL semester 2\dont show me.txt', 'r+')
    
if f.read() == "true":
    gui.close2()
else:
    gui.okButton1()
    gui.showMeAgainButton()
    gui.infomationLabel()    
        
f.close    
root.mainloop()
