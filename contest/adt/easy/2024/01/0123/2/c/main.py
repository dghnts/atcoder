N,M = map(int,input().split())
S = input()
T = input()

if S == T[:len(S)]:
    if S == T[len(T)-len(S):]:
        print(0)
    else:
        print(1)
elif S == T[len(T)-len(S):]:
    print(2)
else:
    print(3)