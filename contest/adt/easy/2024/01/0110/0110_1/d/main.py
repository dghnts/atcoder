S = [int(x) for x in input()]

rane = []

rane.append(S[6])
rane.append(S[3])
rane.append(S[7]+S[1])
rane.append(S[4]+S[0])
rane.append(S[8]+S[2])
rane.append(S[5])
rane.append(S[9])

if S[0] != 0:
    print("No")
else:
    for i in range(5):
        if rane[i] != 0 and rane[i+1] == 0 and rane[i+2] != 0:
            print("Yes")
            exit()
    print("No")