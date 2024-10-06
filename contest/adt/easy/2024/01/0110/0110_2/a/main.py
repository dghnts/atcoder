A,B,C,D = map(int,input().split())

ans = ["Takahashi","Aoki"]
count = 1

t = 3600*A+60*B
s = 3600*C+60*D+1

if t < s:
    count = 0

print(ans[count])    