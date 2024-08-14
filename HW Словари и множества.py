my_dict = {'Denis' : 1996, 'Ivan' : 2000, 'Max' : 1993}
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get('Ilya'))
print(my_dict.get('Ilya', "Такого ключа нет"))
my_dict.update({'Ilya' : 2002,
                'Dani' : 2001})
print(my_dict)
a = my_dict.pop('Dani')
print(a)
my_set = {1, 3, 2, 4, 5, 1, 2}
print(my_set)
print(my_set.add(6))
print(my_set.add(7))
print(my_set)
print(my_set.discard(1))
print(my_set.remove(2))
print(my_set)

