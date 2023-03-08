import random
from prettytable import PrettyTable


m = int(input("Введіть розмір двовимірного списку від 5-ти включно: "))
matrix = [[random.randrange(0,51) for y in range(m)] for x in range(m)]#Створили матрицю
help_list = [0]*m
for i in range(0, m):#Підраховуємо суму стовпців для подальшого перетворення
    for j in range(0, m):
        help_list[i] += matrix[j][i]


def global_sort(matrix_to_sort, list_to_sort):
    for x in range(0, m):#сортуємо стовпці по порядку
            for y in range(0, m-x-1):
                if list_to_sort[y] > list_to_sort[y + 1]:
                    list_to_sort[y], list_to_sort[y + 1] = list_to_sort[y + 1], list_to_sort[y]
                    for j in range(0, m):
                        matrix_to_sort[j][y], matrix_to_sort[j][y + 1] = matrix_to_sort[j][y + 1], matrix_to_sort[j][y] #відсортували стовпці по порядку
    # print("no sort", matrix_to_sort)
    for x in range(1, m, 2):#сортуємо стовпці по зростанню
        for j in range(0, m):
            for y in range(0, m-j-1):
                if matrix_to_sort[y][x] > matrix_to_sort[y+1][x]:
                    matrix_to_sort[y][x], matrix_to_sort[y+1][x] = matrix_to_sort[y+1][x], matrix_to_sort[y][x]
                    # print(matrix_to_sort)
    for x in range(0, m, 2):#сортуємо стовпці по спаданню
        for j in range(0, m):
            for y in range(0, m-j-1):
                if matrix_to_sort[y][x] < matrix_to_sort[y+1][x]:
                    matrix_to_sort[y][x], matrix_to_sort[y+1][x] = matrix_to_sort[y+1][x], matrix_to_sort[y][x]
                    # print(matrix_to_sort)
    return (matrix_to_sort, list_to_sort)


def pretty_print(sorted_matrix, list1):
    newTable = PrettyTable(range (1, m+1))
    for j in range(0, m):
        newTable.add_row(sorted_matrix[j])
    newTable.add_row(list1)
    return (newTable)

print("Вихідна матриця має вигляд:\n", pretty_print(matrix, help_list))
global_sort(matrix, help_list)
print("Результат:\n", pretty_print(matrix, help_list))


