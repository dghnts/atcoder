Y = int(input())

ans = Y

if Y % 4 == 0:
    ans += 2
elif Y % 4 == 1:
    ans += 1
elif Y%4 == 3:
    ans += 3

print(ans)