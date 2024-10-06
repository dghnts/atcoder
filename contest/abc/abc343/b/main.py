N = int(input())

for i in range(N):
    ans = []
    for i, a in enumerate(list(map(int, input().split()))):
        if a == 1:
            ans.append(i+1)
    print(*sorted(ans))
