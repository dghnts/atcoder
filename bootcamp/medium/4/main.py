S = input()
N = len(S)

'''
while True:
    N = len(S)
    if N % 2 == 0:
        flag = True
        for i in range(N//2):
            if S[i] != S[i+N//2]:
                flag = False
                break
        if flag:
            print(N)
            exit()
        else:
            S = S[:-2]
    else:
        S = S[:-1]
'''

for i in range(N//2):
    S = S[:-2]
    M = len(S)//2
    if S[:M] == S[M:]:
        print(M*2)
        exit()
