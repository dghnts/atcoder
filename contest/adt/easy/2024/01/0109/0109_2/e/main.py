import string

X = input()
N = int(input())

# 小文字のアルファベットの文字列
alphabets = list(string.ascii_lowercase)

f = {}
g = {}

for i in range(26):
    f[X[i]] = alphabets[i]
    g[alphabets[i]] = X[i]

S = []

for i in range(N):
    s = list(input())
    for j in range(len(s)):
        s[j] = f[s[j]]
    S.append(s)

S.sort()

for i in range(N):
    t = list(S[i])
    for j in range(len(t)):
        t[j] = g[t[j]]
    print("".join(t))