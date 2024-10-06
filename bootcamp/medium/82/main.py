n = int(input())
a = list(map(int, input().split()))

ave1 = (sum(a)+n-1)//n
res1 = 0

ave2 = sum(a)//n
res2 = 0

for i in range(n):
    res1 += (a[i]-ave1)**2

for j in range(n):
    res2 += (a[j]-ave2)**2

print(min(res1, res2))
