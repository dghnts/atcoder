N, M = map(int, input().split())

A = [int(x) for x in input().split()]

max_cost = sum(A)
a = min(A)

if max_cost <= M:
    print("infinite")
else:
    print(M//N)
