N = int(input())
A = [int(x) for x in input().split()]

'''
rider = 0
for i in range(N):
    if rider+A[i] <= 0:
        rider = 0
    else:
        rider += A[i]
print(rider)
'''

ans = sum(A)

m = 0
sum_Ai = 0

for i in range(N):
    sum_Ai += A[i]
    m = min(m, sum_Ai)

print(ans-m)
