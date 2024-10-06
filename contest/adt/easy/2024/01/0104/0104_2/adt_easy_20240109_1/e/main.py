N, M = map(int, input().split())

A = [int(x) for x in input().split()]

scores = [i+1 for i in range(N)]

not_solves = [[] for _ in range(N)]

for i in range(N):
    s = input()
    for j in range(M):
        if s[j] == "o":
            scores[i] += A[j]
        else:
            not_solves[i].append(A[j])
    not_solves[i].sort(reverse=True)


max_score = max(scores)

for i in range(N):
    if scores[i] == max_score:
        print(0)
        continue
    else:
        count = 0
        while True:
            if scores[i] >= max_score:
                print(count)
                break
            scores[i] += not_solves[i][count]
            count += 1