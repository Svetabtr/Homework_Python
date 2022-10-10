# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите степень мнгочлена k: '))
rate = [randint(0, 10) for i in range(k + 1)]

print(rate)

temps = []
for ratio in rate:
    if ratio:
        if k == 0: ratio = ratio
        elif ratio == 1: ratio = ''
        else: ratio = ratio
    
    if k == 1:  power = 'x'
    elif k == 0: power = ''
    else: power = f'x^{k}'

    temp = f'{ratio}{power}'
    temps.append(temp)

    k-=1

polynom = ' + '.join(temps) + ' = 0'
print(polynom)
    

with open('file_4.4.txt', 'w', encoding = 'utf-8') as data:
    data.write(polynom)

#4 раза пересмотрела семинар, но не получается не выводить коэфициенты 0
