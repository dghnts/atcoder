A,B = input().split()

length = max(len(A), len(B))

A = A.zfill(length)
B = B.zfill(length)

flag = True
for i in range(length):
    if int(A[i])+int(B[i]) > 9:
        flag = False

print("Easy" if flag else "Hard")