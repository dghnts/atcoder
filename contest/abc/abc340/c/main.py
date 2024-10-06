'''
N = int(input())

count = len(bin(N-1)[2:])

ans = 0

if N != 2**count:
    count -= 1
for i in range(count):
    ans += (2+i)*2**i

N -= 2**count
# print(N)

print(ans+(2+count)*N)
'''

# memo化再帰
from functools import cache


@cache
def f(N):
    if N == 1:
        return 0
    else:
        return f(N // 2) + f((N+1)//2)+N


print(f(int(input())))
