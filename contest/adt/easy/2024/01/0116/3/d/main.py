N = int(input())
A = {int(x) for x in input().split()}

for i in range(2001):
    if i not in A:
        print(i)
        break