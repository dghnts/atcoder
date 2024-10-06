N = int(input())
A = [int(x) for x in input().split()]

B = [x for x in A]

count = 0

while True:
    B = sorted(B,reverse=True)
    if B[0] == 0 or B[1] == 0:
        break
    B[0] -= 1
    B[1] -= 1
    #print(B)
    count += 1

print(count)
