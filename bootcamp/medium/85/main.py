s = input()

alph = [False for _ in range(26)]

for i in range(len(s)):
    alph[ord(s[i])-ord('a')] = True

if len(s) < 26:
    s += chr(ord('a')+alph.index(False))
else:
    chars = []
    for i in range(25, -1, -1):
        chars.append(s[i])
        if s[i] >= s[i-1]:
            break
    chars.sort()
    # print(chars)
    if i != 0:
        for j in range(len(chars)):
            if s[i-1] < chars[j]:
                char = chars[j]
                break
        s = s[:i-1]+char
    else:
        s = -1

print(s)
