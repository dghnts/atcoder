N = int(input())
S = input()

for i in range(N-1):
    count = 0
    while True:
        # print(S[count+i+1], S[count])
        if count == N-1-i:
            print(count)
            break
        if S[i+count+1] != S[count]:
            count += 1
        else:
            print(count)
            break
