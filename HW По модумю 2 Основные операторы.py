n = int(input("Введите число от 3 до 20:"))
result = ""

for i in range(1, n+1):
    for j in range(1, n+1):
        if i + j == n and i != j:
            result += str(i) + str(j)

print(result)
