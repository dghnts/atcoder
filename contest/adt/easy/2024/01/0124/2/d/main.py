N,S,M,L = map(int,input().split())

ans = 10**100

for i in range(100):
    for j in range(100):
        for k in range(100):
            if 6*i+8*j+12*k >= N:
                ans = min(ans,S*i+M*j+L*k)

print(ans)