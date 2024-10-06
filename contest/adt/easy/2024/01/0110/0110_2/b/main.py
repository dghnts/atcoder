S = list(input())

n = len(S)//2

for i in range(n):
    S[2*i],S[2*i+1] = S[2*i+1],S[2*i]

print("".join(S))