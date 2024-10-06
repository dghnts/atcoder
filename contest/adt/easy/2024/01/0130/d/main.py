from copy import deepcopy
M = int(input())
D = [int(x) for x in input().split()]

med = (sum(D)+1)//2

day = deepcopy(med)

i = 0

while True:
    if day <= D[i]:
        month = i+1
        break
    day -= D[i]
    i += 1

print(month, day)
