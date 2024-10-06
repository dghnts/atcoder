S = list(input())
T = list(input())

for i in range(len(S)-1):
    if S[i] != T[i]:
        S[i],S[i+1] = S[i+1],S[i]
        break

if "".join(S) == "".join(T):
    print("Yes")
else:
    print("No")