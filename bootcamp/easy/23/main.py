N = int(input())
D, X = map(int, input().split())

choco = 0

for i in range(N):
    A = int(input())
    choco += (D-1)//A+1

print(choco+X)
