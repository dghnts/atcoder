from collections import defaultdict
import math
N = int(input())
A = [int(x) for x in input().split()]
dict = defaultdict(int)

ans = 0
for i in range(N):
    d = math.floor(math.sqrt(A[i]))
    if A[i] == 0:
        dict[0] += 1
    else:
        while True:
            if A[i] % (d**2) == 0:
                dict[A[i] // (d**2)] += 1
                break
            else:
                d -= 1
#    print(ans)

# print(dict)

for v in dict.values():
    ans += v*(v-1)//2

ans += dict[0]*(N-dict[0])

print(ans)
