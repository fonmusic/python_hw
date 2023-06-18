# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3) 
# 100 -> 1 (1 + 0 + 0)

# number = int(input('введите натуральное число: '))

input = number = 123
sum = 0
while number > 0:
    remainder = number % 10
    sum = sum + remainder
    number //= 10

print(f'{input} -> {sum}')


input = number = 100
sum = 0
while number > 0:
    remainder = number % 10
    sum = sum + remainder
    number //= 10

print(f'{input} -> {sum}')
