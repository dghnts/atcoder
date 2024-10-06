N, Y = map(int, input().split())

for i in range(N+1):
    for j in range(N-i+1):
        if N-i-j >= 0 and 1000*i+5000*j+10000*(N-i-j) == Y:
            print(N-i-j, j, i)
            exit()

print(-1, -1, -1)
