n = 6
poison = 'anton'
lines = [
    '222anton456', 
    'a1n1t1o1n1', 
    '0000a0000n00t00000o000000n', 
    'gylfole', 
    'richard', 
    'ant0n']

infected = []

for i in range(n):
    found = True
    for j in poison:
        if j not in lines[i]:
            found = False
            break
        else:
            lines[i] = lines[i][lines[i].index(j):] 
            print(lines)
            infected.append(j)
    if found:
        print(i + 1, end=' ')
   

print(infected)
