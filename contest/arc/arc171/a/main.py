T = int(input())

'''
for i in range(T):
    N, A, B = map(int, input().split())
    flag = True
    if A > N:
        flag = False
    else:
        if B > min(N-A, (N+1)//2)*(N-A):
            flag = False
    print("Yes" if flag else "No")
'''

for i in range(T):
    N, A, B = map(int, input().split())
    flag = True
    if A > N:
        flag = False
    else:
        cell = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N//2):
