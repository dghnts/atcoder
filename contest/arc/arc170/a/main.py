N = int(input())

S = list(input())
T = list(input())

ans = 0
start = 0

if S != T:
    while True:
        if S[start] != T[start]:
            break
        start += 1

    S = S[start:]
    T = T[start:]

    if T[0] == "B":
        ans = -1
    else:
        for i in range(len(S)):
            if S[i] != T[i] and T[i] == "B":
                ans += 1

print(ans)
