# Task2
value_list = None
test_list = []
black_exit = None
test_list = input("Введите значение массива(списка) через пробел: ").split()
# print(len(test_list2))
test_list2 = test_list[0:]
for el in range (0, len(test_list2), 2):
    # print(test_list2.index(el))
    if el == len(test_list2) - 1:
        break
    else:
        test_list2[el], test_list2[el + 1] = test_list2[el + 1], test_list2[el]
    # print(el, test_list2)
print("Преобразованный список ", test_list2)
