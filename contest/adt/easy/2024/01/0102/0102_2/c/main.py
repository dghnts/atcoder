import math
N = int(input())

coordinates = []
ans = 0

for i in range(N):
    coordinates.append(tuple(map(int, input().split())))

for i in range(N):
    a = coordinates[i]
    for j in range(i + 1, N):
        b = coordinates[j]
        dist = math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
        ans = max(ans, dist)

print(ans)