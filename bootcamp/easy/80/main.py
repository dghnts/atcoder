N = int(input())

ans = float('inf')

i = 1

while i**2 < N+1:
    if N % i == 0:
        ans = min(ans, i+N//i-2)
    i += 1
print(ans)
