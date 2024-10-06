H, W = map(int, input().split())

ans = [0 for _ in range(W)]

for i in range(H):
    c = input()
    for i in range(W):
        if c[i] == "#":
            ans[i] +=1

print(*ans)