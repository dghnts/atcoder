N = int(input())

J = []

for j in range(1,10):
    if N % j == 0:
        J.append(N//j)
 
ans = ""

for i in range(N+1):
    for j in J:
        if i % j == 0:
            ans += str(N//j)
            break
    if len(ans) != i+1:
        ans += "-"

print(ans)