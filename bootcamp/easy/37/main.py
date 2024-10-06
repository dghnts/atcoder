N, K, Q = map(int, input().split())

points = [K-Q for _ in range(N)]

for i in range(Q):
    A = int(input())
    points[A-1] += 1

for i in range(N):
    if points[i] <= 0:
        print("No")
    else:
        print("Yes")
