N = int(input())
S = list(input())
Q = int(input())

alph = {chr(ord("a")+i): chr(ord("a")+i) for i in range(26)}

for i in range(Q):
    c, d = input().split()
    for k, v in alph.items():
        if v == c:
            alph[k] = d
# print(alph)
for i in range(len(S)):
    S[i] = alph[S[i]]


print("".join(S))
