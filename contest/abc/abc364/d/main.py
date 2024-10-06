N, Q = map(int, input().split())

a = [int(x) for x in input().split()]

for i in range(Q):
    c = [int(x) for x in a]
    b, k = map(int, input().split())
    c = sorted([abs(x-b) for x in c])
    print(c[k-1])
