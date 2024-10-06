N = int(input())
A = sorted([int(x) for x in input().split()])

even = []
odd = []
for a in A:
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)
ans = -1
if len(even) >= 2:
    ans = max(even[-1]+even[-2], ans)
if len(odd) >= 2:
    ans = max(even[-1]+even[-2], ans)

print(ans)
