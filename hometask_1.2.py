# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = 1
Y = 1
Z = 1

res1 = bool(not (X or Y or Z))
res2 = bool(not X and not Y and not Z)

print(bool(res1== res2))

# 2 вариант

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'X={x}, Y={y}, Z={z}')
            print(not (x or y or z) == (not x and not y and not z))
            print()


# 3 вариант

values = False, True
print( all(not (x or y or z) == (not x and not y and not z) for x in values for y in values for z in values))