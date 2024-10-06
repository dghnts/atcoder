N, M = map(int, input().split())
S = input()

# 0で区切られた連続した数字の文字列をリストにする
continuous_char = S.split("0")

ans = 0
for s in continuous_char:
    #1文字列に1が含まれるかどうかを判定する
    if "1" in s:
        ans = max(ans, len(s)-min(s.count("1"), M))
    else:
        ans = max(ans, len(s))

print(ans)
