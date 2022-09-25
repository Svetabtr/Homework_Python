# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = 1
Y = 1
Z = 1

res1 = bool(not (X or Y or Z))
res2 = bool(not X and not Y and not Z)

print(bool(res1== res2))