S = input()
n = len(S)

ans = set()

for i in range(n):
    for j in range(i, n):
        ans.add(S[i:j+1])

print(len(ans))
