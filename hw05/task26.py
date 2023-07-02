# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит 
# число А в целую степень B с помощью рекурсии.
# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 


def pow_recursive(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / pow_recursive(a, - b)
    return a * pow_recursive(a, b - 1)

a = 3
b = 5

res = pow_recursive(a, b)

print(f'A = {a}; B = {b} -> {res}')