s = input()
n = len(s)

dic = {"a": 0, "b": 0, "c": 0}

for i in range(n):
    dic[s[i]] += 1

for k in dic.keys():
    for l in dic.keys():
        if abs(dic[k]-dic[l]) > 1:
            print("NO")
            exit()
print("YES")
