S = input()

flag = True

if S[0] != "A":
    flag = False

if "C" not in S:
    flag = False
elif not (1 < S.index("C") and S.index("C") < len(S)-1):
    flag = False

count = 0
for s in S:
    if s.islower():
        count += 1
if count != len(S)-2:
    flag = False

print("AC" if flag else "WA")
