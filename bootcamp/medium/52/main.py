n = int(input())

time_cost = [[i, 0] for i in range(n)]
time_limit = [[i, 0] for i in range(n)]

for i in range(n):
    time_cost[i][1], time_limit[i][1] = map(int, input().split())

time_limit = sorted(time_limit, key=lambda x: x[1])

time = 0

for i, limit in time_limit:
    if time+time_cost[i][1] <= limit:
        time += time_cost[i][1]
    else:
        # print(time, time_cost[i][1], limit)
        print("No")
        exit()
print("Yes")
