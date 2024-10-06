N = int(input())
A = [int(a) for a in input().split()]

ans = 1
for a in A:
    if a % 2 == 0:
        ans *= 2
    else:
        ans *= 1
print(3**N-ans)
