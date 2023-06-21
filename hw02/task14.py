# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = 100

power = 0
result = 0
while 2**power <= N:
    result = 2**power
    print(f'2 в степени {power} равно {result}')
    power += 1



