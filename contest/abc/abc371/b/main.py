N, M = map(int, input().split())
house = [[] for _ in range(N)]

for i in range(M):
    A, B = input().split()
    A = int(A)-1
    if B == "M" and "M" not in house[A]:
        print("Yes")
    else:
        print("No")
    house[A].append(B)
