from collections import defaultdict

S = input()

dict = defaultdict(int)

for s in S:
    dict[s] += 1
    
mx = max(dict.values())

ans = []

for key in dict.keys():
    if dict[key] == mx:
        ans.append(key)

print(sorted(ans)[0])