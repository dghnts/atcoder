H, W = map(int, input().split())
A = []

for r in range(H):
    A.append(list(input()))
"""
rcut = []
for r in range(H):
    if set(A[r]) == {"."}:
        rcut.append(r)

B = []

for c in range(W):
    row = []
    for r in range(H):
        row.append(A[r][c])
    B.append(row)

ccut = []
for r in range(W):
    if set(B[r]) == {"."}:
        ccut.append(r)

# print(rcut, ccut)
ans = []
for r in range(H):
    row = []
    if r in rcut:
        continue
    for c in range(W):
        if c in ccut:
            continue
        row.append(A[r][c])
    ans.append(row)

for i in range(len(ans)):
    print("".join(ans[i]))
"""

row_num = [False for _ in range(H)]
column_num = [False for _ in range(W)]

for r in range(H):
    for c in range(W):
        if A[r][c] == "#":
            row_num[r] = True
            column_num[c] = True

for r in range(H):
    if row_num[r]:
        row = []
        for c in range(W):
            if column_num[c]:
                row.append(A[r][c])
        print("".join(row))
