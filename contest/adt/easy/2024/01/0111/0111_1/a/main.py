N, M, P = map(int, input().split())

ans = 0
while True:
    if M+P*ans > N:
        break
    ans += 1

print(ans)