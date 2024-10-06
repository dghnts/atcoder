S = input()

char = set()

for s in S:
    if s not in char:
        char.add(s)
    else:
        print("no")
        exit()
print("yes")
