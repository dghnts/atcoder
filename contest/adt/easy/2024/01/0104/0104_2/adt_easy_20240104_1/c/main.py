N = int(input())

S = []

for i in range(N):
    S.append(input())

for j in range(N):
    for k in range(N):
        if j == k:
            continue
        else:
            flag=True
            T = S[j]+S[k]
            for l in range(len(T)):
                if T[l] != T[len(T)-l-1]:
                    flag = False
            if flag:
                print("Yes")
                exit()
print("No")