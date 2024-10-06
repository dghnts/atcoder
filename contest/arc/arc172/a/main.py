H, W, N = map(int, input().split())
A = sorted([int(x) for x in input().split()], reverse=True)

chocolate = [["#" for _ in range(W)] for _ in range(H)]

for i in range(N):
