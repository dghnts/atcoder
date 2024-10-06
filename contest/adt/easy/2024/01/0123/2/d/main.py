N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

count1 = 0
count2 = 0

for i in range(N):
    if A[i] in B:
        if A[i] == B[i]:
            count1 += 1
        else:
            count2 += 1

print(count1)
print(count2)            