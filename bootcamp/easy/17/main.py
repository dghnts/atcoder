N = int(input())
v = [int(x) for x in input().split()]
v.sort()

ans = v[0]
for i in range(N):
    ans += v[i]
    ans /= 2

print(ans)
