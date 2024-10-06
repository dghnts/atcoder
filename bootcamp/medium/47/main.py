N, P = map(int, input().split())
A = [int(a) for a in input().split()]

odd = False

for a in A:
    if a % 2 == 1:
        odd = True
        break

if P == 0:
    if odd:
        ans = 2**(N-1)
    else:
        ans = 2**N
else:
    if odd:
        ans = 2**(N-1)
    else:
        ans = 0
print(ans)
