N = int(input())
H = [int(x) for x in input().split()]

length = 0
ans = 0
for i in range(N):
    length = max(H[i], length)
    if length == H[i]:
        ans = i+1
print(ans)
