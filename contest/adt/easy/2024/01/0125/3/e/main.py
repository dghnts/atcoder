N = int(input())
N = bin(N)[2:]

ans = ""
for i in range(len(N)):
    if N[i] == "1":
        ans += "A"
    if i != len(N)-1:
        ans += "B"

print(ans) 