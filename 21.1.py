import random

m = int(input("Введіть кількість рядків: "))
n = int(input("Введіть кількість колонок: "))
matrix = [[random.randrange(0,51) for y in range(n)] for x in range(m)]#Створили матрицю\
print("Згенерована матриця:", matrix)


def sum_ryadok(matrix_to_sum):
    sum = [0]*m
    for x in range(0, m):
        for y in range(0, n):
            sum[x] += matrix_to_sum[x][y]
    return (sum)


def sum_kolonka(matrix_to_sum):
    sum = [0]*n
    for x in range(0, n):
        for y in range(0, m):
            sum[x] += matrix_to_sum[y][x]
    return (sum)

def print_funk(matrix_to_sum):
    summary = sum_ryadok(matrix_to_sum)
    for x in range(0, len(matrix_to_sum)):
        for y in range(0, n):
            print('{:<4}'.format(matrix_to_sum[x][y]), end="  ")
        print('      ', '{:<4}'.format(summary[x]))

    print("\n")
    summary = sum_kolonka(matrix_to_sum)
    for y in range(0, n):
        print('{:<4}'.format(summary[y]), end="  ")

print("\n\nРезультат:")
print_funk(matrix)
print("\n\n")
# print_funk(sum_kolonka(matrix))