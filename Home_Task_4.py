# Task4
a = input("Введите строку: ")
my_list = a.split()
# print(a)
for el in range (0, len(my_list)):
    print(f"\n№{el+1} {str(my_list[el])[:10]}")

