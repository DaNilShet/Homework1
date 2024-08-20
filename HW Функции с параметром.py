def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
n = int(input('Кол. строк'))
m = int(input('Кол. столбцов'))
value = input(f'Значение')
print('-------' * m)
matrix = get_matrix(n, m, value)
if n <= 0:
    print('Матрица пуста')
elif m <= 0:
    print('Матрица пуста')
else:
    print('Матрица готова:')
    for i in matrix:
        print(*i)
