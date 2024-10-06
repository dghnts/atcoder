S = input()

flag = [False for _ in range(10)]

for s in S:
    flag[int(s)] = True

print(flag.index(False))