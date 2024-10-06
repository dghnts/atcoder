N, Q = map(int, input().split())
R = [int(x) for x in input().split()]
R.sort()
query = {}
for i in range(Q):
    query.append(int(input()))
    count = 0
    i = -1
    while True:
        i += 1
        if i> len(R)-1:
            ans = len(R)
            break
        if count+R[i] > X:
            ans= i
            break
        count += R[i]
    print(ans)