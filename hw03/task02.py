# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, 6]
k = 6

closest = None
min_diff = None

for num in list_1:
    if num > k:
        diff = num - k
    else:
        diff = k - num
    if min_diff is None or diff < min_diff:
        min_diff = diff
        closest = num

print(closest)