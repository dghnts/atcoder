N, T = map(int, input().split())
t = [int(x) for x in input().split()]

time = T*N
for i in range(N-1):
    time -= max(0, T-t[i+1]+t[i])
print(time)
