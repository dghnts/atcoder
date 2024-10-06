S = input()
T = "oxx"*(10**5)

l = 0
r = len(S)
for i in range(len(T)-len(S)):
    if T[l:r] == S:
        print("Yes")
        exit()
    else:
        l += 1
        r += 1

print("No")