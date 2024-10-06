N, K = map(int, input().split())
A = list(map(int,input().split()))

socks = []
for i in range(N):
    socks.append(i)
    if i in A:
        socks.append(i)

ans = 0

while True:
    if len(socks) == 0:
        break
    if len(socks) == 1:
        ans += socks[0]
        break
    
    sock_1 = socks.pop(-1)
    sock_2 = socks.pop(-1)
    ans += abs(sock_1-sock_2)

print(ans)