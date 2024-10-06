n = int(input())
a = [int(x) for x in input().split()]

dic = {x: 0 for x in set(a)}

res = 0

for i in range(n):
    dic[a[i]] += 1

for k, v in dic.items():
    if k < v:
        res += v-k
    elif k > v:
        res += v

print(res)
