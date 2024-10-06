import itertools
import math
N = int(input())

coords = []

for i in range(N):
    coord = [int(x) for x in input().split()]
    coords.append(coord)

"""
ptn = list(itertools.permutations(list(range(N))))

dists = []

for p in ptn:
    dist = 0
    for i in range(len(p)-1):
        a = coords[p[i]]
        b = coords[p[i+1]]
        # print(a, b)
        dist += math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    dists.append(dist)

print(sum(dists)/len(ptn))
"""

dist = 0

for i in range(N):
    for j in range(i+1, N):
        dist += math.sqrt((coords[i][0]-coords[j][0])**2 +
                          (coords[i][1]-coords[j][1])**2)

print(dist*2/N)
