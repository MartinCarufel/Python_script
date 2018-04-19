#coding:utf-8

from math import ceil
from random import shuffle
from tkinter import *


class Player:
    def __init__(self):
        self._ent1 = ""
        self.p_list = []

    def _get_ent1(self):
        return self._ent1

    def _set_ent1(self, new):
        print("Add player")
        self._ent1 = new

    ent1 = property(_get_ent1, _set_ent1)

    def edit_player(self, p_name=""):
        win2 = Tk()
        win2.title(p_name)
        lab = Label(win2, text=p_name)
        lab.pack()

    def add_player(self, tx, name):
        """Class constructor"""
        self.tx = tx
        self.p_list.append(name.get())

        #tx.insert(END, name.get()+"\n")
        tx.delete(1.0,END)
        for i in self.p_list:
            tx.insert(END, i+"\n")

        # print("Button affiche: {}".format(tx_aff.get()))
        # print(ent1.get())
        #but2 = Button(win1, text=tx_aff.get(), command=lambda: edit_player(name.get()))
        #but2.pack()
        #print(type(but2))
        print(self.p_list)

class App(Frame):
    def __init__(self, win1, **kwargs):
        Frame.__init__(self, **kwargs)

        ent1 = Entry()
        tx = Text(win1)

        but1 = Button(win1, text="Add player", command=lambda: player.add_player(tx, ent1))
        ent1.pack()
        but1.pack()
        tx.pack()
        print("loop")


player = Player()

win1 = Tk()
app = App(win1)
win1.mainloop()


#d = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
shuffle(player.p_list)

d_copy = list(player.p_list)
nb_par_table = 8

#for i in range (0, ceil(len(d)/nb_par_table)):
#    table.append("Table{}".format(i))

table = {"table"+ str(i+1): "" for i in range (ceil(len(player.p_list)/nb_par_table))}
table_list = table.keys()
table_l = []
for i in table_list:
    table_l.append(i)

#print(type(table_list))


for i in range(len(table_l)):

    start = i*len(player.p_list)//len(table)
    end = (i*len(player.p_list)//len(table))+len(player.p_list)//len(table)
    dx = player.p_list[start:end]
    temp = {table_l[i]:dx}
    table.update(temp)
    remain_item = list(set(d_copy).difference(set(dx)))
    d_copy = list(remain_item)

for i in range(len(remain_item)):
    #add_value = "{}".format(table.get(table_l[i])) + remain_item[i]
    add_value = list(table.get(table_l[i]))
    add_value.append(remain_item[i])
    temp = {table_l[i]: add_value}
    table.update(temp)

#table_list[0] = "allo"
print(table_l)
print(table)
print(remain_item)
