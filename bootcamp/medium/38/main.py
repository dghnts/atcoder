from collections import defaultdict
N = int(input())
D = [int(D) for D in input().split()]
M = int(input())
T = [int(T) for T in input().split()]

dic_D = defaultdict(int)
dic_T = defaultdict(int)

for d in D:
    dic_D[d] += 1

for t in T:
    dic_T[t] += 1

flg = True
if N < M:
    flg = False
else:
    for k, v in dic_T.items():
        if k not in dic_D.keys():
            flg = False
        elif dic_D[k] < v:
            flg = False

print("YES" if flg else "NO")
