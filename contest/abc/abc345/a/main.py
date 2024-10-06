S = input()

if S[0] != "<" or S[-1] != ">":
    print("No")
    exit()
else:
    for i in range(1, len(S)-1):
        if S[i] != "=":
            print("No")
            exit()
print("Yes")
