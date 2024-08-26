def print_params (a = 1, b = "строка", c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ["Здравствуйте", 1475, [15, 12, 36]]
values_dict = {'a': [1, 2, 3], 'b': 'Здравствуйте02', 'c': 1475}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['ABC', [1.124, 4752, 1475]]
print_params(*values_list_2, 35)