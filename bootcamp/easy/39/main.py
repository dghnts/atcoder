N = int(input())
A = []

for i in range(N):
    A.append(int(input()))
'''
B = sorted(A)
M = B[-1]
m = B[-2]

for a in A:
    if a != M:
        print(M)
    else:
        print(m)
'''

left = [0]
right = [0]

for i in range(N):
    left.append(max(left[-1], A[i]))
    right.append(max(right[-1], A[N-i-1]))

# print(left, right)
for i in range(N):
    print(max(left[i], right[-i-2]))
