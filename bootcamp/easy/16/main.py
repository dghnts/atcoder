from collections import defaultdict

N = int(input())
A = [int(x) for x in input().split()]

'''
dict = defaultdict(int)

for i, a in enumerate(A):
    dict[a] = i+1

dict = sorted(dict.items(), key=lambda x: x[0])

ans = [int(x[1]) for x in dict]

print(*ans)
'''

ans = [0 for _ in range(N)]

for i, a in enumerate(A):
    ans[a-1] = i+1

print(*ans)
