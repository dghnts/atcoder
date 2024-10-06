from collections import defaultdict
N, M = map(int, input().split())

dic = defaultdict(int)

for i in range(N):
    A, B = map(int, input().split())
    dic[A] += B

dic = sorted(dic.items())

# print(dic)
ans = 0

for i in range(N):
    if M-dic[i][1] <= 0:
        ans += M*dic[i][0]
        break
    else:
        ans += dic[i][0]*dic[i][1]
        M -= dic[i][1]

print(ans)
