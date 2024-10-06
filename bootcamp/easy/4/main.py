N = int(input())

for i in range(N+1):
    x = i*10.8//10
    if x == N:
        print(i)
        exit()
print(":(")
