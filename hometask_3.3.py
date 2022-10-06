# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.45, 1.87, 3.21, 5, 10.01]
new_lst = []
for i in lst:
    new_lst.append(round(i - int(i),2))

print(new_lst)

def FindMax(new_lst):
    max_value = new_lst[0]
    for i in new_lst:
        if i > max_value:
            max_value = i
    return(max_value)

def FindMin(new_lst):
    min_value = new_lst[0]
    for i in new_lst:
        if i < min_value:
            min_value = i
    return(min_value)

print(f'Разница максимального и минимального остатка = ', FindMax(new_lst) - FindMin(new_lst))
