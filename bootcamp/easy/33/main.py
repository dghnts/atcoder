A, B = map(int, input().split())
S = input()

flag = True

for i in range(A+B+1):
    if i != A and S[i] not in [str(j) for j in range(10)]:
        flag = False
    if i == A and S[i] != "-":
        flag = False
    if not flag:
        break
print("Yes" if flag else "No")
