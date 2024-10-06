A, B, C = map(int, input().split())


for i in range(101):
    num = A * i
    if num % B == C:
        print("YES")
        exit()
print("NO")
