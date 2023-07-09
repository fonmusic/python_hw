# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indices_in_range(arr, min_value, max_value):
    indices = []
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            indices.append(i)
    return indices

my_list = [1, 5, 10, 15, 20, 25, 30]
minimum = 10
maximum = 25

result = find_indices_in_range(my_list, minimum, maximum)
print("Индексы элементов в заданном диапазоне:", result)
