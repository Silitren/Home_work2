# Task5
my_list = [7, 5, 3, 3, 2]
print('Для выхода введите 0')
a = None
while a != 0:
    a = int(input('число: '))
    for el in range(len(my_list)):
        if a == my_list[el]:
            my_list.insert(el + 1, a)
            # print(my_list[el] == a, el < len(my_list))
            break
        elif a > my_list[el]:
            my_list.insert(el, a)
            break
        # else:
        #     my_list.append(a)
        #     break
    # else:
    #     my_list.append(a)
    print(my_list)
