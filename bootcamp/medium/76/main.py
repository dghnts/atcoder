n = int(input())
s = input()

total_left = [0 for _ in range(n)]
total_right = [0 for _ in range(n)]

for i in range(n-1):
    total_left[i+1] = total_left[i]
    if s[i] == "W":
        total_left[i+1] += 1
for i in range(n-1, 0, -1):
    total_right[i-1] = total_right[i]
    if s[i] == "E":
        total_right[i-1] += 1
res = n

# print(total_left)
# print(total_right)

for i in range(n):
    res = min(res, total_left[i]+total_right[i])
print(res)
