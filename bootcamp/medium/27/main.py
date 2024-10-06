N = int(input())
s = input()
t = input()

# 最長で2*N
ans = N

'''
# sのi文字目以降とtの文字列が一致しているかチェック
for i in range(N):
    if s[i:] == t[:N-i]:
        ans -= N-i
        break
'''

for i in range(N):
    flg = True
    for counter in range(N-i):
        if s[i+counter] != t[counter]:
            flg = False
            break
    if flg:
        ans += i
        break
    if i == N-1:
        ans += N

print(ans)
