N = int(input())

names = set()
flag = False
for i in range(N):
    name = tuple(input().split())
    if name not in names:
        names.add(name)
    else:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")

