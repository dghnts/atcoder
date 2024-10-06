S = list(input())
N = len(S)

'''
white = []
black = []

for i, s in enumerate(S):
    if s == "W":
        white.append(i)
    else:
        black.append(i)

count = 0
for i, w in enumerate(white):
    count += w-i

for j, b in enumerate(black):
    count += N-1-b-j

print(count//2)
'''

black = 0
count = 0

for i in range(N):
    if S[i] == "B":
        black += 1
    else:
        count += black

print(count)
