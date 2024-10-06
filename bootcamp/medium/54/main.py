n, c, k = map(int, input().split())

arrives = []

for i in range(n):
    arrives.append(int(input()))

arrives.sort()

bus = 1
limit = arrives[0]+k
passenger = 0

count = 0

for i in range(n):
    if arrives[i] <= limit and passenger < c:
        passenger += 1
        continue
    passenger = 1
    bus += 1
    limit = arrives[i]+k


print(bus)
