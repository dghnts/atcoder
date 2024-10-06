S = input()
N = len(S)

countzero = 0
countone = 0
for s in S:
    if s == "1":
        countone += 1
    else:
        countzero += 1

print(2*min(countone, countzero))
