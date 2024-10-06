from collections import defaultdict
N, K = map(int, input().split())

nums = defaultdict(int)

A = [int(x) for x in input().split()]


for a in A:
    nums[a] += 1

nums = sorted(nums.items(), key=lambda x: x[1])
count = len(nums)

if count <= K:
    print(0)
else:
    ans = 0
    i = 0
    while True:
        if count == K:
            break
        else:
            ans += nums[i][1]
            count -= 1
            i += 1
    print(ans)
