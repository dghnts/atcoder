N,X = map(int, input().split())
A = {int(x) for x in input().split()}

for a in  A:
    if a+X in A:
        print("Yes")
        exit()
print("No")