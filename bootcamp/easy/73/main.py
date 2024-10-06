N = int(input())
n = N
count = 0
while True:
    if N//10 == 0:
        break
    N //= 10
    count += 1

ans = 9*count

if n % 10**count == 10**(count)-1:
    ans += N
else:
    ans += N-1


print(ans)
