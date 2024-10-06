N = int(input())

div = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = 0

for n in range(1, N + 1):
    if n % 10 == 0:
        div = [int(x) + 1 for x in div]
    if n % div[n % 10] == 0:
        ans += 1
    if n== N:
        print(n%div[n%10])
print(ans)
