from string import ascii_lowercase
S = input()

alph = {x: 0 for x in list(ascii_lowercase)}

for s in S:
    alph[s] = 1

ans = "None"
for k in alph.keys():
    if alph[k] != 1:
        ans = k
        break
print(ans)
