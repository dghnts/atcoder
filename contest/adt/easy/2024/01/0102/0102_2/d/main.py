S = input()
T = input()

flag = True

if len(S) <= len(T):
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        else:
            flag = False
            break
else:
    flag = False

if flag:
    print("Yes")
else:
    print("No")