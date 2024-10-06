N = int(input())
T = [int(t) for t in input().split()]
origin_time = sum(T)
M = int(input())
'''
for i in range(M):
    p, x = map(int, input().split())
    diff_time = T[p-1]-x
    print(origin_time-diff_time)
'''

for i in range(M):
    p, x = map(int, input().split())

    x, T[p-1] = T[p-1], x
    print(sum(T))
    T[p-1] = x
