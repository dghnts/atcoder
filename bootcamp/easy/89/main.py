X, Y = map(int, input().split())

seq = [X]

while seq[-1]*2 <= Y:
    seq.append(seq[-1]*2)

print(len(seq))
