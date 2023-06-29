# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random


n = 11
m = 6

# first version

nums1 = []
nums2 = []

for _ in range(n):
    random_number = random.randint(0, 10)
    nums1.append(random_number)

for _ in range(m):
    random_number = random.randint(0, 10)
    nums2.append(random_number)

print(nums1)
print(nums2)

unique_nums = set()

for i in nums1:
    for j in nums2:
        if i == j:
            unique_nums.add(i)

res = sorted(unique_nums)
print(res)

# second version
print('--------------------------------')

nums1 = [random.randint(0, 10) for _ in range(n)]
nums2 = [random.randint(0, 10) for _ in range(m)]

print(nums1)
print(nums2)

unique_nums = set(nums1).intersection(nums2)
res = sorted(unique_nums)

print(res)