N = int(input())
A = [int(x) for x in input().split()]

dic = {}

for a in A:
    if a not in dic.keys():
        dic[a] = 1
    else:
        dic[a] += 1

ans = 0
for key in dic.keys():
    n = dic[key]
    ans += n*(n-1)//2

for i in range(N):
    print(ans-dic[A[i]]+1)
