N = int(input())
A = [int(a) for a in input().split()]

if 1 not in A:
    print(-1)
else:
    ans = A.index(1)
    num = 2
    for i in range(ans+1, N):
        if A[i] != num:
            ans += 1
        else:
            num += 1
    print(ans)
