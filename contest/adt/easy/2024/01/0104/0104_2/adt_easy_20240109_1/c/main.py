from copy import deepcopy

N = int(input())
S = input()

ans = deepcopy(S)

count = 0
for i in range(len(S) - 1):
    if S[i] == "n" and S[i + 1] == "a":
        ans = ans[: i + 1 + count] + "y" + ans[i + 1 + count :]
        count += 1

print(ans)
