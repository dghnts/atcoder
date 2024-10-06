from collections import defaultdict
N, M = map(int, input().split())

dic = defaultdict(set)
win = []
for i in range(M):
    a, b = map(int, input().split())
    
    dic[b].add(a)

for i in range(N):
    for key in dic.keys():
        if i in dic[key]:
            dic[key] = dic[key].union(dic[i])

for key in dic.keys():
    if len(dic[key]) == N-1:
        win.append(key)
        
if len(win) != 1:
    print(-1)
else:
    print(win[0])