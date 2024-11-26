my_list = [42, 69, 322, 13, 0, 99, 9, 8, 7, 5]
index_lst = 0
print(len(my_list))
while my_list[index_lst] > 0:
    if my_list[index_lst] == 0:

        continue
    if (my_list[index_lst]) >= len(my_list):
            print(my_list[index_lst])
            index_lst += 1
            continue
    else:
        break
