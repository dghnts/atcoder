from math import sin, cos, radians

N = int(input())

line = []
for i in range(N):
    line.append(list(map(int, input().split())))

line = sorted(line)

for i in range(N):
    for j in range(i + 1, N):
        chk = line[i] + line[j]
        count = 0
        for k in range(3):
            if chk[k] > chk[k + 1]:
                chk[k], chk[k + 1] = chk[k + 1], chk[k]
                count += 1
                print(chk)
        if count == 1:
            print(chk)
            print("Yes")
            exit()
print("No")
