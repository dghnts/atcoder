A, B, K = map(int, input().split())

count = A
ans = 0

while count < B:
    count *= K
    ans += 1
print(ans)
