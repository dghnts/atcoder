N = int(input())
W = list(input().split())

chk = ["and", "not", "that", "the", "you"]

for w in W:
    if w in chk:
        print("Yes")
        exit()
print("No")
