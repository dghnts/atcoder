import itertools

N = int(input())
P = tuple([int(x) for x in input().split()])
Q = tuple([int(x) for x in input().split()])

permutations = itertools.permutations([i for i in range(1, N+1)], N)

permutations = list(permutations)

print(abs(permutations.index(Q)-permutations.index(P)))
