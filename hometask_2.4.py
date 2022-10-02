# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

lst = [random.randint(-50, 50) for i in range(100)]

print(lst)

mult = 1
data = open('file.txt', 'r')

for line in data:
    line = int(line)
    mult *= lst[line]
   
print('Произведение чисел = ', mult)
data.close()
# print(lst[45], lst[20], lst[4], lst[92], lst[10])