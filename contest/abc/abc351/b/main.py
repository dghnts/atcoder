n = int(input())
a = []
b = []
for i in range(n):
    a.append(input())
for i in range(n):
    b.append(input())

for i in range(n):
    if a[i] != b[i]:
        for j in range(n):
            if a[i][j] != b[i][j]:
                print(i+1, j+1)
