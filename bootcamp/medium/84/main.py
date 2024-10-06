n = int(input())
L = [int(x) for x in input().split()]
L.sort(reverse=True)

left = 0
right = n-1

for i in range(n):
    for j in range(n-1):
