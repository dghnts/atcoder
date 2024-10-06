n = int(input())
a = [int(x) for x in input().split()]

res = a[0] ^ a[1]
for i in range(2, n):
    res ^= a[i]

if not res:
    print("Yes")
else:
    print("No")
