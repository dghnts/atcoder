from collections import defaultdict
N = int(input())
A = [int(a) for a in input().split()]

len_dic = defaultdict(int)

for a in A:
    len_dic[a] += 1

len_dic = sorted(len_dic.items())

tate = 0
yoko = 0

for v in len_dic[::-1]:
    if tate == 0:
        if v[1] > 1:
            tate = v[0]
            if v[1]-2 > 1:
                yoko = v[0]
                break
    elif v[1] > 1:
        yoko = v[0]
        break

print(tate*yoko)
