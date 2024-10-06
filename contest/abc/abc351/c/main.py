n = int(input())
a = [int(x) for x in input().split()]

res = []

for i in range(n):
    res.append(a[i])
    while True:
        if len(res) < 2:
            break
        if res[-1] != res[-2]:
            break
        else:
            res[-1] = res.pop()+1
print(len(res))
