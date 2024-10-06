N = int(input())
A = [int(x) for x in input().split()]

divide_count = []

for i, a in enumerate(A):
    divide = 0
    while True:
        if a % 2 != 0:
            divide_count.append(divide)
            break
        else:
            a //= 2
            divide += 1
print(sum(divide_count))
