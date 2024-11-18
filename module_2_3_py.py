my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_lst = -1

while index_lst < len(my_list):
    index_lst = index_lst + 1

    if my_list[index_lst] == 0:

        continue
    elif my_list[index_lst] < 0:

        break
    else:
        print(my_list[index_lst])
