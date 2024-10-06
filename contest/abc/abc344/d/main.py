S = ""
T = input()
N = int(input())
A = []
bags = []
for i in range(N):
    a = input(), [s for s in input().split()]
    A.append(a[0])
    bag = a[1:]
    bags.append(bag)

j = 0
while True:
    if j == N:
