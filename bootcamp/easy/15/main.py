from collections import defaultdict

N = int(input())
d = [int(x) for x in input().split()]

dict = defaultdict(int)

for i in range(N):
    dict[d[i]] += 1

if N % 2 != 0:
    print(0)
    exit()
else:
    count = 0
    keys = sorted(dict.keys())
    for i in range(len(keys)):
        count += dict[keys[i]]
        if count == N//2:
            print(keys[i+1]-keys[i])
            exit()
print(0)
