S = input()
N = len(S)

for i in range(N):
    for j in range(i+1, N):
        new_s = S[:i+1]+S[j:]
        if new_s == "keyence":
            print("YES")
            exit()
print("NO")
