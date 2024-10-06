from collections import defaultdict
N = int(input())
S = list(map(int, input().split()))

dic = defaultdict(int)
check = {}
for s in S:
    dic[s] += 1
    if not s in check.keys():
        check[s] = False
        
ans = 0

for a in range(1,251):
    for b in range(a,251):
        n = 4*a*b+3*a+3*b
        if n in check.keys():
            if check[n] == False:
                ans += dic[n]
                check[n] = True
                
print(N-ans)