from collections import defaultdict
n, m = map(int, input().split())

teiki = defaultdict(list)
flg = True

if m < 2:
    flg = False
else:
    for i in range(m):
        a, b = map(int, input().split())
        teiki[a].append(b)

    for i in teiki[1]:
        if n in teiki[i]:
            flg = True
            break
        else:
            flg = False

if flg:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
