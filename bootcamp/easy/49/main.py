H, W = map(int, input().split())

ans = []
for i in range(H+2):
    if i == 0 or i == H+1:
        ans.append("#"*(W+2))
    else:
        ans.append("#"+input()+"#")

for i in range(H+2):
    print(ans[i])
