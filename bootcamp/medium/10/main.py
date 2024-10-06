N = int(input())
A = [int(a) for a in input().split()]
S = set()
dic = {i: 0 for i in range(-1, 10**5+10)}
for a in A:
    S.add(a)
    dic[a] += 1

ans = 0
for a in S:
    ans = max(ans, dic[a-1]+dic[a]+dic[a+1])

print(ans)
