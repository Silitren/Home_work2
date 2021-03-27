# Task6
product = []
i = 0
while input("\nВведите данные товара\n(для продолжения нажмите enter, для выхода 'q'): ") != "q":
    i += 1
    product.append(i)
    product.append(
        dict({
        'название': str(input("Введите название товара: ")),
        'цена': float(input("Введите цену: ")),
        'количество': int(input("Введите количество: ")),
        'СИ': str(input("Введите единицу измерения: ")),
        })
        )

print(f'\n{product}')

analitic = dict()
for el in range(1, len(product), 2):
    for key, value in product[el].items():
        if key in analitic:
            if value not in analitic.get(key):
                analitic[key].append(value)
        else:
            analitic.update({key: [value]})

analys = 'y'
if analys == input('\nВывести аналитку? (y/n): '):
    print()
    for key, value in analitic.items():
        print(key, value)
    else:
        exit()




