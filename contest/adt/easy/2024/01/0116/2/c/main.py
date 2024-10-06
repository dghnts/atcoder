T = int(input())

for i in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for a in A:
        if a%2 != 0:
            ans +=1
    print(ans)
    