# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Пример:
# 6782 -> 23
# 0,56 -> 11

num = str(input("Введите число: "))
num = num.replace('.', '').replace(',', '')

if num.isdigit():
    num = int(num)
    res = 0

    while num != 0:
        res = res + num % 10
        num =num // 10
    print('Сумма цифр = ', res)
    
else:
    print("Это не число")






