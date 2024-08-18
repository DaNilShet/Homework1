first = int(input('Первое'))
second = int(input('Второе'))
third = int(input('Третье'))

if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third:
    print('Вывод: 2')
else:
    print('Вывод: 0')