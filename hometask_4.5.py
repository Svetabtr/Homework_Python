# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def read_file(file):
    with open(str(file)) as data:
        tmp = data.read()
    return tmp

file1 = 'file_4.5_1.txt'
file2 = 'file_4.5_2.txt'

poly1 = read_file(file1).replace(' = 0', '')
poly2 = read_file(file2).replace(' = 0', '')


poly = poly1.split(' + ') + poly2.split(' + ')
print('Слагаемые от полученных полиномов = ', poly)
 
result = {}  

# честно сворованная часть кода
for term in poly:
    if 'x^' in term:
        ratio, power = map(lambda x: int(x) if x else 1, term.split('x^'))
        result[power] = result.get(power, 0) + ratio
    elif 'x' in term:
        ratio, _ = map(lambda x: int(x) if x else 1, term.split('x'))
        result[1] = result.get(1, 0) + ratio
    else:
        result[0] = result.get(0, 0) + int(term)
 
# print(result)
 
result = sorted(result.items(), reverse = True)
# print(result)
terms = []
for power, ratio in result:
    ratio = ratio if power == 0 else '' if ratio == 1 else ratio
    power = 'x' if power == 1 else '' if power == 0 else f'x^{power}'
    term = f'{ratio}{power}'
 
    terms.append(term)
 
# print(terms)
sum_poly = ' + '.join(terms) + ' = 0'
print('Результат сложения полиномов: ', sum_poly)

with open('file_4.5_res.txt', 'w', encoding = 'utf-8') as data:
    data.write(sum_poly)