#coding:utf-8

from math import ceil
from random import shuffle

d = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
shuffle(d)

d_copy = list(d)
nb_par_table = 8

#for i in range (0, ceil(len(d)/nb_par_table)):
#    table.append("Table{}".format(i))

table = {"table"+ str(i+1): "" for i in range (ceil(len(d)/nb_par_table))}
table_list = table.keys()
table_l = []
for i in table_list:
    table_l.append(i)

#print(type(table_list))


for i in range(len(table_l)):

    start = i*len(d)//len(table)
    end = (i*len(d)//len(table))+len(d)//len(table)
    dx = d[start:end]
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
