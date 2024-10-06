N, K = map(int, input().split())
A = set(int(a) for a in input().split())

# print(A)

sum = K*(K+1)//2

for a in A:
    if a <= K:
        sum -= a

print(sum)
