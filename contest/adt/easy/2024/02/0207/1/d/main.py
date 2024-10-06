import itertools
N, M = map(int, input().split())

people = [i+1 for i in range(N)]

pairs = list(itertools.combinations(people, 2))
# print(pairs)

dic = {pair: False for pair in pairs}

for i in range(M):
    a = list(map(int, input().split()))
    for i in range(N-1):
        if a[i] < a[i+1]:
            p = (a[i], a[i+1])
        else:
            p = (a[i+1], a[i])
        if p in dic:
            dic[p] = True
print(len(dic.values())-sum(dic.values()))
