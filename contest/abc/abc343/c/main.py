N = int(input())

for x in range(10**6+10):
    K = x**3
    if K < N+1:
        K = str(K)
        # print(K)
        if list(K) == list(K)[::-1]:
            ans = K
    else:
        break
print(ans)
