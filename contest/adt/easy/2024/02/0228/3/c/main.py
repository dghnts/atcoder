S = input()
N = len(S)

chk = {"xox", "oxx", "xxo"}
short = {"xo", "ox", "xx"}
flag = True

while True:
    if len(S) == 0 or not flag:
        break
    if len(S) >= 3:
        if S[:3] in chk:
            S = S[3:]
        else:
            flag = False
    else:
        if S not in short:
            flag = False
        S = ""

print("Yes" if flag else "No")
