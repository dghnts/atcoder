N = int(input())
A = list({int(x) for x in input().split()})
M = int(input())
B = list({int(x) for x in input().split()})
L = int(input())
C = list({int(x) for x in input().split()})

nums = set()
for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(C)):
            nums.add(A[i]+B[j]+C[k])

Q = int(input())
X = [int(x) for x in input().split()]

for x in X:
    if x in nums:
        print("Yes")
    else:
        print("No")
