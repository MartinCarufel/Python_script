#coding:utf-8

import pyautogui
from tkinter import *

posx = 0
posy = 0
root = Tk()
coord = Label(root, text="x={} , y= {}" .format(posx, posy))
coord.pack()

width, height = pyautogui.size()
print("Largeur {}, hauteur {} de l'ecran" .format(width, height))
#pyautogui.moveTo(width/2, height/2)






while(True):
    posx, posy = pyautogui.position()
    coord = Label(root, text="x={} , y= {}".format(posx, posy))
    Label.update(root)


root.mainloop()
