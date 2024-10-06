from collections import defaultdict
N = int(input())

count = defaultdict(int)

for i in range(N):
    a = int(input())
    count[a] += 1
    count[a] %= 2

print(sum(count.values()))
