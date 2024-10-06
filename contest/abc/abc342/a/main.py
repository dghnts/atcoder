from collections import defaultdict
S = input()

dict = defaultdict(int)

for s in S:
    dict[s] += 1

for key in dict.keys():
    if dict[key] == 1:
        print(S.index(key)+1)
