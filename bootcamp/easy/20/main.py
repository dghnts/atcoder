def f(n, s):
    if n == 0:
        return s
    if n % 2 == 0:
        return n//2
    else:
        return 3*n+1


s = int(input())

i = 0
a = []

while True:
    if len(set(a)) != i:
        print(i)
        break
    if i == 0:
        a.append(s)
    else:
        a.append(f(a[i-1], s))
    i += 1
    # print(nums)
