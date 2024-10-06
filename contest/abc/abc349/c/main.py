S = input()
T = input().lower()

if T[-1] == "x":
    T = T[:-1]

i = 0
for s in S:
    if T[i] == s:
        i += 1
        if i == len(T):
            print("Yes")
            exit()
print("No")
