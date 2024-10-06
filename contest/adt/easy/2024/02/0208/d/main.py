N = int(input())
H = [int(x) for x in input().split()]

num = 0

while True:
    if num == N-1 or H[num] >= H[num+1]:
        break
    num += 1

print(H[num])
