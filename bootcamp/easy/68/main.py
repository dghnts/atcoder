from collections import defaultdict
N = int(input())

restaurants = []

for i in range(N):
    city, point = input().split()
    restaurants.append((i+1, city, point))

restaurants = sorted(restaurants, key=lambda x: x[1])

restaurants = sorted(restaurants, key=lambda x: (x[1], -1*int(x[2])))

for i in range(N):
    print(restaurants[i][0])
