N = int(input())
A = [int(a) for a in input().split()]

one = 0
two = False
four = 0

for i in range(N):
    count = 0
    while True:
        if A[i] % 2 != 0:
            if count == 0:
                one += 1
            elif count == 1:
                two = True
            else:
                four += 1
            break
        else:
            A[i] //= 2
            count += 1

if two:
    one += 1

if one <= four+1:
    print("Yes")
else:
    print("No")
