# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, 
# список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]


import random
array = [random.randint(0, 10) for i in range(20)]
print(array)

arr_without_doubles = []
arr_doubles = []
arr_unic = array.copy()

for i in array:
    if i not in arr_without_doubles: arr_without_doubles.append(i)
    elif i not in arr_doubles: arr_doubles.append(i)

for i in array: 
    if i in arr_doubles: arr_unic.remove(i)


print(f'Список уникальных: {arr_unic}')
print(f'Список дублей: {arr_doubles}')
print(f'Список без дублей: {arr_without_doubles}')
