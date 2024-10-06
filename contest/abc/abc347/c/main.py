n, a, b = map(int, input().split())
# 曜日を1,2,3,...,A+B-1となるように設定する
# 0,1,...,A-1までが休日
# A,A+1,...,A+B-1が平日
d = [int(x) % (a+b) for x in input().split()]

mx = 0
mn = 10*10

for i in range(1, n):
    dx = (d[i]-d[0]) % (a+b)
    if dx >= a:
        dx -= a+b
    mx = max(mx, dx)
    mn = min(mn, dx)

if mx-mn < a:
    print("Yes")
else:
    print("No")
