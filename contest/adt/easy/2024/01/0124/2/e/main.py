def need_time(needs):
    for need in needs:
        ans = T[need-1]
        if A[need-1] == {0}:
            return ans
        else:
            ans += need_time(A[need])
            
N = int(input())
T = []
K = []
A = []

for i in range(N):
    arts = list(map(int,input().split()))
    T.append(arts[0])
    K.append(arts[1])
    if K != 0:
        A.append(set(arts[2:]))
    else:
        A.append(set([0]))

ans = 0

print(need_time(A[-1]))