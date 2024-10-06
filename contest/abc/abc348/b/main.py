n = int(input())

x = [0]*100
y = [0]*100

for i in range(n):
    x[i], y[i] = map(int, input().split())

for i in range(n):
    dist = (x[i]-x[0])**2+(y[i]-y[0])**2
    res = 1
    for j in range(n):
        dist_test = (x[i]-x[j])**2+(y[i]-y[j])**2
        if dist < dist_test:
            dist = dist_test
            res = j+1
    print(res)
