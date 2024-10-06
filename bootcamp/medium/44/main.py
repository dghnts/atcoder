from collections import deque
n = int(input())
a = [int(x) for x in input().split()]

flag = True

ans = deque()

for i in range(n):
    if i % 2 == 0:
        ans.append(a[i])
    else:
        ans.appendleft(a[i])
    flag = not flag

if flag:
    print(*ans)
else:
    print(*list(ans)[::-1])
