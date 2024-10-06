from collections import defaultdict
N = int(input())

counts = []
nums = []

for i in range(N):
    C = int(input())
    A = [int(x)for x in input().split()]
    counts.append(C)
    nums.append(A)

X = int(input())

# print(nums)

ans = defaultdict(list)
for i in range(N):
    if X in nums[i]:
        ans[counts[i]].append(i+1)

if len(ans.keys()) != 0:
    num = min(ans.keys())
    print(len(ans[num]))
    print(*ans[num])
    exit()

print(0)
