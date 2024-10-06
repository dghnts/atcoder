S = input()

upper = False
lower = False
chk = set()

for i, s in enumerate(S):
    # print(s)
    if s.isupper():
        upper = True
    elif s.islower():
        lower = True
    chk.add(s)
    if i+1 != len(chk):
        print("No")
        exit()

if upper and lower:
    print("Yes")
else:
    print("No")
