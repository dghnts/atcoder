A, B, C = map(int, input().split())
'''
total = A+B+C
count = 0
a, b, c = A, B, C
while True:
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        print(count)
        break
    a, b, c = (total-a)//2, (total-b)//2, (total-c)//2
    count += 1
    if a == A and b == B and c == C:
        print(-1)
        break
'''

if A == B and B == C:
    if A % 2 == 0:
        print(-1)
    else:
        print(0)
else:
    count = 0
    while True:
        if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
            print(count)
            break
        A, B, C = (B+C)//2, (C+A)//2, (A+B)//2
        count += 1
