S = input()

dict = {}

for s in S:
    if s in dict.keys():
        dict[s] += 1
    else:
        dict[s] = 1

for key in dict.keys():
    if dict[key] == 1:
        print(key)
        exit()
print(-1)