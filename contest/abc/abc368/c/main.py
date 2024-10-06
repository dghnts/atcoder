N = int(input())
H = [int(x) for x in input().split()]

T = 0

for h in H:
    num = h//5
    T += 3*num
    h -= 5*num
    while h > 0:
        T += 1
        if T % 3 == 0:
            h -= 3
        else:
            h -= 1

print(T)
