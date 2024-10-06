A = []
for i in range(3):
    A.append([int(x) for x in input().split()])

N = int(input())

bingo = [[False for _ in range(3)] for _ in range(3)]

for i in range(N):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if A[j][k] == b:
                bingo[j][k] = True
# print(bingo)
if bingo[0][0] and bingo[0][1] and bingo[0][2]:
    print("Yes")
elif bingo[1][0] and bingo[1][1] and bingo[1][2]:
    print("Yes")
elif bingo[2][0] and bingo[2][1] and bingo[2][2]:
    print("Yes")
elif bingo[0][0] and bingo[1][0] and bingo[2][0]:
    print("Yes")
elif bingo[0][1] and bingo[1][1] and bingo[2][1]:
    print("Yes")
elif bingo[0][2] and bingo[1][2] and bingo[2][2]:
    print("Yes")
elif bingo[0][0] and bingo[1][1] and bingo[2][2]:
    print("Yes")
elif bingo[0][2] and bingo[1][1] and bingo[2][0]:
    print("Yes")
else:
    print("No")
