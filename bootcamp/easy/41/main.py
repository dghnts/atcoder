N = int(input())
P = [int(x) for x in input().split()]
'''
m = P[0]
ans = 0


for i in range(N):
    m = min(m, P[i])
    # print(m, P[i])
    if m >= P[i]:
        ans += 1

print(ans)
'''

ans = 0

for i in range(N):
    if min(P[:i+1]) == P[i]:
        ans += 1
print(ans)
