n = int(input())
hp = [int(a) for a in input().split()]

res = min(hp)

while True:
    for i in range(n):
        if hp[i] == res:
            j = i
        hp[i] %= res
    if sum(hp) == 0:
        break
    else:
        hp[j] = res
    res = min([x for x in hp if x != 0])

print(res)
