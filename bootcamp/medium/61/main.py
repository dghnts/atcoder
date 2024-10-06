from collections import deque

s = input()
q = int(input())

s = deque(list(s))
flg = False

for i in range(q):
    args = list(input().split())
    q = int(args[0])
    if q == 1:
        flg = not flg
    else:
        f = int(args[1])
        c = args[2]
        if flg:
            if f == 1:
                s.append(c)
            else:
                s.appendleft(c)
        else:
            if f == 1:
                s.appendleft(c)
            else:
                s.append(c)
if flg:
    s = list(s)[::-1]

print("".join(s))
