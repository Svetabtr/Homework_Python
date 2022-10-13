# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
arr = [random.randint(0, 15) for i in range(20)]

print(arr)

new_arr = []
for i in arr:
    if arr.count(i) < 2:
        new_arr.append(i)
    
print (new_arr)

