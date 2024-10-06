N, A, B = map(int, input().split())
C = [int(x) for x in input().split()]

ans = A+B

print(C.index(ans)+1)
