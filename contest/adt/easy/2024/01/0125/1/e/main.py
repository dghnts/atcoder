def count_num(n):
    if n == 2:
        return 3
    else:
        return 3*count_num(n-1)-1

N = int(input())

if N==2:
    print(count_num(N)*9-2)
else:
    print(count_num(N)*9)