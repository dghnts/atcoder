N = int(input())
dic = {i+1: int(x) for i, x in enumerate(input().split())}

dic = sorted(dic.items(), key=lambda x: x[1])

print(dic[-2][0])
