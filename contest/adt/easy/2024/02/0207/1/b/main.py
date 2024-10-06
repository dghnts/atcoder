from string import ascii_uppercase
N, X = map(int, input().split())

alph = ascii_uppercase
# S = ""

# for i in range(26):
#    S += ascii_uppercase[i]*N

# print(S)
# print(S[X-1])

print(alph[(X-1)//N])
