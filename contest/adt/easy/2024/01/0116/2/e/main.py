def rle(s):
    pair_s = []
    cnt = 1
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            pair_s.append(tuple([s[i - 1], cnt]))
            cnt = 0
        cnt += 1

    pair_s.append(tuple([s[-1], cnt]))

    return pair_s


S = list(input())
T = list(input())

flag = True

i = 1

pair_S = rle(S)
pair_T = rle(T)

if len(pair_S) != len(pair_T):
    print("No")
    exit()

ans = True

for i in range(len(pair_S)):
    if pair_S[i][0] != pair_T[i][0]:
        ans = False

    if not (
        pair_S[i][1] == pair_T[i][1]
        or pair_S[i][1] < pair_T[i][1]
        and pair_S[i][1] >= 2
    ):
        ans = False
        break

print("Yes" if ans else "No")
