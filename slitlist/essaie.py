# coding: utf-8

x_dic = {"a": [1, 2, 3, 4], "b": ["aa", "bb", "cc"]}

for i, j in x_dic.items():
#for i in x_dic.keys():
    print("La table {} contient les joueur {}" .format(i, j))