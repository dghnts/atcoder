N, M = map(int,input().split())

flag = True

B = []

rows = []
col = 0
for r in range(N):
    b = [int(x) for x in input().split()]
    i = b[0] // 7
    j = b[0] % 7
    
    if r == 0:
        col = j
    elif col != j:
        flag = False
        break
    if rows == []:
        rows.append(i)
    else:
        print(rows[-1])

        if rows[-1]+1 != i:
            flag = False
            break
        else:
            rows.append(i)
    
    if flag:        
        for c in range(M):
            if b[c] != 7*i + j+c:
                flag = False
                break
        if not flag:
            break

print("Yes" if flag else "No")