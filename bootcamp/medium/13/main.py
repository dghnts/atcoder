N = int(input())

p = (0, 0)
T = [0]

for i in range(N):
    t, x, y = map(int, input().split())
    cd = (x, y)

    dist = abs(cd[0]-p[0])+abs(cd[1]-p[1])
    dt = t-T[-1]
    # print(dist, dt)
    if dist <= t-T[-1] and dist % 2 == (t-T[-1]) % 2:
        T.append(t)
        p = cd
    else:
        print("No")
        exit()

print("Yes")
