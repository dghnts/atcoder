S = input()

flag = True

if S[0].islower():
    flag = False
for i in range(1,len(S)):
    if S[i].isupper():
        flag = False   
        break

print("Yes" if flag else "No")