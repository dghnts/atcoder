x, y = map(int, input().split())

res = 0
if x == 0:
    res += abs(y)
    if y < 0:
        res += 1
elif y == 0:
    res += abs(x)
    if x >= 0:
        res += 1
else:
    if y < x:
        if x < 0:
            res += 1
            res += abs(y)-abs(x)
            res += 1
        elif 0 < y:
            res += 1
            res += abs(x)-abs(y)
            res += 1
        else:
            res += 1
            res += abs(abs(x)-abs(y))
    if x < y:
        if y < 0:
            res += abs(x)-abs(y)
        elif 0 < x:
            res += y-x
        else:
            res += 1
            res += abs(abs(x)-abs(y))

print(res)
