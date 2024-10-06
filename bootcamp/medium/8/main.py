N = int(input())
A = [int(a) for a in input().split()]

color = set()
count = 0
flag = False
for a in A:
    if a >= 3200:
        flag = True
        count += 1
    else:
        color.add(a//400)

if flag:
    if len(color) == 0:
        m = 1
    else:
        m = len(color)
    M = len(color)+count
else:
    m = len(color)
    M = len(color)

print(m, M)
