A, B = map(int,input().split())

count = A
ans = 1
while True:
    if count >= B:
        break
    count += A-1
    ans += 1

print(ans)