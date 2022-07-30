# Задача: предложить улучшения кода для уже решённых задач с помощью использования **лямбд, 
# filter, map, zip, enumerate, list comprehension
# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

import random
n = int(input("Введите количество элементов последовательности:"))
col = [random.randint(-n,n) for i in range(n)]
unique_col = [i for i in col if col.count(i) == 1]
print(f'Уникальные элементы последовательности {col} равны\n {unique_col}')

# Найти сумму чисел списка стоящих на нечетной позиции

def odd_index(numbers):
    new_numbers = []
    index = 1
    while index in range(len(numbers)):
        new_numbers.append(numbers[index])
        index += 2
    return new_numbers
n = int(input("Введите количество элементов последовательности:"))
col = [random.randint(-n,n) for i in range(n)]
print(f'На нечетных позициях списка {col} стоят числа {odd_index(col)} их сумма равна: {sum(map(int, odd_index(col)))}')

# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Введите количество элементов последовательности:"))
col = {i: 3*i +1 for i in range(n+1)}
del col[0]
print(col)