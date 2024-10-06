N,P = map(int,input().split())
a = [int(x) for x in input().split()]

ans = 0

for score in a:
    if score < P:
        ans += 1

print(ans)