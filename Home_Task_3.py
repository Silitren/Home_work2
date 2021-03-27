# Task3
season = dict(q1='Зима', q2='Весна', q3='Лето', q4='Осень')
q1 = (12, 1, 2)
q2 = (3, 4, 5)
q3 = (6, 7, 8)
q4 = (9, 10, 11)
a = int(input())
if a in q1: print(season.get('q1'))
if a in q2: print(season.get('q2'))
if a in q3: print(season.get('q3'))
if a in q4: print(season.get('q4'))
# for el in range (1, 5):
#     b = eval('q' + str(el))
#     с = 'q' + 'el'
#     # print(b)
#     if a in b:
#         print(season.get(b))
#         break
