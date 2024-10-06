from collections import defaultdict
S = input()

dic = defaultdict(int)

for s in S:
    dic[s] += 1

dic_num = defaultdict(int)

for v in dic.values():
    dic_num[v] += 1

# print(dic_num)
for v in dic_num.values():
    if v != 2:
        print("No")
        exit()
print("Yes")
