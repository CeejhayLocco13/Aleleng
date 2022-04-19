from tkinter import *

top = Tk()
top.title("Label")
top.geometry("400x250")


Lab = Label(top, text="Laboratory Activity 5").place(x = 200, y = 100, anchor="center")
Prof = Label(top, text = "Submitted to: Mam Sayo").place(x = 200, y = 140,anchor="center")

top.mainloop()

#Text Field Window
from tkinter import *

window = Tk()

window.title("Text Field")
window.geometry("350x150")

txtfld = Entry(window,bd=1, font=("Arial",11))
txtfld.place(x=75,y=40,width=200,height=75)


window.mainloop()


#Father of Computer Window
from tkinter import *
import tkinter.font as font

window = Tk()


window.title("Father of computer")
window.geometry("700x500")

label = Label(window, text="Charles Babbage", bg = "#09ebee",fg = "black", font= "Arial 50")
label.place(x=100, y=200)

window.mainloop()


#4 
from tkinter import *

top = Tk()

top.title("Major Subjects")

top.geometry("250x250")

listbox = Listbox(top)

listbox.insert(1,"reading")

listbox.insert(2, "writing")

listbox.insert(3, "arithmetic")

listbox.insert(4, "coding")

listbox.pack()

top.mainloop()

#Button Window
from tkinter import *

class MyButton:
    def __init__(self,window):
        self.btn1 = Button(window, text='Color', fg="Red", bg='Blue')
        self.btn1.place(x=50, y=100)
        self.btn2 = Button(window,text='<---Click to change the color of the button',command=self.colorChange)
        self.btn2.place(x=100, y=100)

    def colorChange(self):
        self.btn1.configure(bg="Yellow")

window = Tk()
mywin = MyButton(window)
window.title("Button")
window.geometry("350x150")
window.mainloop()
