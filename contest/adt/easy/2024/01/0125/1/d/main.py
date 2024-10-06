S = input()

chkb = 0
chkrk = 0

for i, s in enumerate(S):
    if s == "B":
        chkb += i
    if s == "R":
        chkrk += 1
    if s == "K" and chkrk + 1 != 2:
        print("No")
        exit()

if chkb % 2 == 0:
    print("No")
else:
    print("Yes")
