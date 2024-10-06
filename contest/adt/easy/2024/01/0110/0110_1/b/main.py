N = int(input())
S = list(input())

flag = {"A":0, "B":0, "C":0}

for i,s in enumerate(S):
    flag[s] = 1
    if sum(flag.values()) == 3:
        print(i+1)
        break