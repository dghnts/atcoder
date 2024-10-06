H = int(input())

attack = 1

if H != 1:
    i = 1
    while True:
        if H // 2 == 0:
            break
        else:
            H //= 2
            attack += 2**i
            i += 1
print(attack)
