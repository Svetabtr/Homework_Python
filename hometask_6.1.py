# # Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

exmpl = '(2+6-2*3)*3/2-(1+5)'
ex = list(exmpl)

# print(ex)
addit = lambda x, y: x + y
sub = lambda x, y: x - y
mult = lambda x, y: x * y
div = lambda x, y: x / y

def find_hooks(ex):
    for el in ex:
        if el == '(':
            index1 = ex.index(el)
    for el in ex:
        if el == ')':
            index2 = ex.index(el)
    hooks = ex[index1+1:index2]

    math_multiplication(hooks)
    math_division(hooks)
    math_addition(hooks)
    math_subtraction(hooks)

    ex[index1:index2+1] = hooks

    return ex

def math_multiplication(ex):
    for el in ex:
        if el == '*':
            index = ex.index(el) 
            res= mult(float(ex[index-1]), float(ex[index+1]))
            ex[index-1:index+2] = [res]
    return ex

def math_division(ex):
    for el in ex:
        if el == '/':
            index = ex.index(el) 
            res = div(float(ex[index-1]), float(ex[index+1]))
            ex[index-1:index+2] = [res]
    return ex

def math_addition(ex):
    for el in ex:
        if el == '+':
            index = ex.index(el) 
            res = addit(float(ex[index-1]), float(ex[index+1]))
            ex[index-1:index+2] = [res]
    return ex

def math_subtraction(ex):
    for el in ex:
        if el == '-':
            index = ex.index(el) 
            res = sub(float(ex[index-1]), float(ex[index+1]))
            ex[index-1:index+2] = [res]
    return ex

while '(' in ex:
    hooks = find_hooks(ex)
math_multiplication(ex)
math_division(ex)
math_addition(ex)
math_subtraction(ex)
# print(hooks)

# print(ex)
print(f'{exmpl}={ex[0]}')

# print(eval(exmpl))
    

    

