S = input()

ACGT = {"A", "C", "G", "T"}
ans = ""
pre = ""

for s in S:
    if s in ACGT:
        pre += s
    else:
        pre = ""
    if len(pre) > len(ans):
        ans = pre


print(len(ans))
