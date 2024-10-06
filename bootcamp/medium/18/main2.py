c = []

for i in range(3):
    c.append(list(map(int, input().split())))

a = [0 for _ in range(3)]
b = [c[0][i] for i in range(3)]

a[1] = c[1][0]-c[0][0]
a[2] = c[2][0]-c[0][0]

for i in range(3):
    for j in range(3):
        if c[i][j] != a[i]+b[j]:
            print("No")
            exit()
print("Yes")
