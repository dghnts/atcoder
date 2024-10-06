N = int(input())
words = list()
for i in range(N):
    w = input()
    if w not in words:
        words.append(w)
    else:
        print("No")
        exit()
    if w[i][-1] != w[i][0]:
        print("No")
        exit()
    if i == N-1:
        print("Yes")
