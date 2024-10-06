N = int(input())
A = [int(a) for a in input().split()]

count = 0

i = 0
while i < N:
    while i+1 < N and A[i] == A[i+1]:
        # print("{}と{}は同じ値です".format(i+1, i+2))
        i += 1
    if i+1 < N ans A[i] < A[i+1]:
        while i+1 < N and A[i] <= A[i+1]:
            i += 1
    elif i+1 < N and A[i] > A[i+1]:
        while i+1 < N and A[i] >= A[i+1]:
            i += 1
    # print("{}番目で区切ります".format(i+1))
    i += 1
    count += 1
print(count)
