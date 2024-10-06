from collections import defaultdict
w = input()

char = defaultdict(int)

for s in w:
    char[s] += 1

flag = True

for v in char.values():
    if v % 2 != 0:
        flag = False
        break

print("Yes" if flag else "No")
