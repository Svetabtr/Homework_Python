# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число: '))
arr = []

while number > 0:
    arr.append(number % 2)
    number = int(number/2)

res= arr[::-1]

for i in res:
    print(res[i], end='')

