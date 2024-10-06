N = int(input())
H = [int(h) for h in input().split()]

for i in range(1, N-1):
    if H[i+1] < H[i]:
        H[i+1] += 1
    if H[i] > H[i+1]:
        print("No")
        exit()

print("Yes")
