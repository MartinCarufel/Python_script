# coding: utf-8

from tkinter import *


root = Tk()
root.geometry("1000x500")

font_helvetica_25 = ("Helvetica", 25, "bold")

can1 = Canvas(height=490, width=990, bg="coral3")
lab1 = Label(text="Allo", font=font_helvetica_25)
can1.create_image(1000,500,image="Trajectoire théorique.JPG")


#lab1.place(x=0, y=466)
can1.place(x=5, y=5)

root.mainloop()