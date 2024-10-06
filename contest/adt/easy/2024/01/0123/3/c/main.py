S = input()

flag = True

if not S[0].isalpha() or not S[-1].isalpha():
    flag = False

N = len(S)

if N != 8:
    flag = False
else:
    for i in range(1,N-1):
        if (i==1 and S[i]=="0") or S[i].isalpha():
            flag=False
            break

print("Yes" if flag else "No")
