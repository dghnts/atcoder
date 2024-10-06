X = int(input())

ans = 0
for i in range(1, X+1):
    if 100*i <= X and 105*i >= X:
        ans = 1
        break
print(ans)
