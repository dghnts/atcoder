A, B, C = map(int, input().split())

if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
    print(0)
else:
    print(min(A*B, B*C, C*A))
