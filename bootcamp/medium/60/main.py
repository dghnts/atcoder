n = int(input())

check = "MARCH"
name_pre = {prefix: 0 for prefix in check}

for i in range(n):
    name = input()
    prefix = name[0]
    if prefix in check:
        name_pre[prefix] += 1

res = 0
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            res += name_pre[check[i]]*name_pre[check[j]]*name_pre[check[k]]

print(res)
