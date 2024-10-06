N = int(input())
D = [int(x) for x in input().split()]

ans = 0

for i in range(N):
    month = set(list(str(i+1)))
    if len(month) != 1:
        continue
    else:
        for day in range(D[i]):
            day = set(list(str(day+1)))
            if day == month:
                ans += 1
        

print(ans)