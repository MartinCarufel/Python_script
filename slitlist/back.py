# coding: utf-8

def create_table(self):
    # d = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
    shuffle(player.p_list)

    d_copy = list(player.p_list)
    nb_par_table = 8

    table = {"table" + str(i + 1): "" for i in range(ceil(len(player.p_list) / nb_par_table))}
    table_list = table.keys()
    table_l = []
    for i in table_list:
        table_l.append(i)

    # print(type(table_list))

    for i in range(len(table_l)):
        start = i * len(player.p_list) // len(table)
        end = (i * len(player.p_list) // len(table)) + len(player.p_list) // len(table)
        dx = player.p_list[start:end]
        temp = {table_l[i]: dx}
        table.update(temp)
        remain_item = list(set(d_copy).difference(set(dx)))
        d_copy = list(remain_item)

    for i in range(len(remain_item)):
        # add_value = "{}".format(table.get(table_l[i])) + remain_item[i]
        add_value = list(table.get(table_l[i]))
        add_value.append(remain_item[i])
        temp = {table_l[i]: add_value}
        table.update(temp)

        print(Player.table_l)
        print(Player.table)
        print(Player.remain_item)
