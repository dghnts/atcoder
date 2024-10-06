from collections import defaultdict
N = int(input())

dic = defaultdict(int)

for i in range(N-1):
    a, b = map(int, input().split())
    dic[a] += 1
    dic[b] += 1

if N-1 in dic.values():
    print("Yes")
else:
    print("No")    