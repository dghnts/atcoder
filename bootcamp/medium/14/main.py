H, W = map(int, input().split())

sckecth = [["."]*(W+2)]*(H+2)

# print(sckecth)

for r in range(1, H+1):
    sckecth[r] = "."+input()+"."

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for r in range(1, H+1):
    for c in range(1, W+1):
        if sckecth[r][c] == "#":
            flag = False
            for i in range(4):
                if sckecth[r+dy[i]][c+dx[i]] == "#":
                    flag = True
            if not flag:
                print("No")
                exit()

print("Yes")
