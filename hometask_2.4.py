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
    print(lst[line])
print('Произведение чисел = ', mult)

print(lst[45], lst[20], lst[4], lst[92], lst[10])
#sum=0

# id - взять сам элемент - id[i]
# lst - взять индекс равный элементу - 

# for i in id:
#     a=lst[i]

#     if id[i] == lst[a]:
#         sum *= id[i]
    
# for line in data:
#     if int(data.readline()) == lst.index(int(data.readline())):
#         print('yes')
#     else:
#         print('no')