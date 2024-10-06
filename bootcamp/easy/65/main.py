S = input()
N = len(S)

for i in range(N):
    if S[i] == "A":
        left = i
        break
for j in range(N-1, -1, -1):
    if S[j] == "Z":
        right = j+1
        break
print(right-left)
