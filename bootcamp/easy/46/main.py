A, B, C, K = map(int, input().split())

if abs(A-B) < 10**18:
    if K % 2 == 0:
        print(A-B)
    else:
        print(B-A)
else:
    print("Unfair")
