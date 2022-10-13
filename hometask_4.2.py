# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите натуральное число N: '))

res = []
d = 2

while N > 1:
    if N % d == 0:
        res.append(d)
        N //= d
    else: 
        d += 1

print (res)