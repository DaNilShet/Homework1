immutable_var_ = 1, 2.0, 'tuple', True
print(immutable_var_)
#immutable_var_[0] = 200 кортеж не поддерживает обращение по элементам
mutable_list_ = ([1, 2.0,] ,'tuple', True)
print(mutable_list_)
mutable_list_[0][0] = 2
print(mutable_list_)
