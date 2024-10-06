N = int(input())

counta = 0

for i in range(N):
    s = input()
    if i == N-1:
        break
    if s == "sweet":
        counta += 1
    else:
        counta = 0
    if counta == 2:
        print("No")
        exit()

print("Yes")
