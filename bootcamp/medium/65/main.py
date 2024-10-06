import math

N, M = map(int, input().split())
s = input()
t = input()

g = math.gcd(N, M)
n = N//g
m = M//g

res = n*m*g

for i in range(g):
    if s[i*n] != t[i*m]:
        res = -1
        break
print(res)
