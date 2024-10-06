N = int(input())
X = [int(x) for x in input().split()]

sorted_X = sorted(X)

judge = (sorted_X[N//2-1]+sorted_X[N//2])/2

for x in X:
    if x < judge:
        print(sorted_X[N//2])
    else:
        print(sorted_X[N//2-1])
