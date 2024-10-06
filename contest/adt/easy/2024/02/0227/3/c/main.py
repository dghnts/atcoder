N, M = map(int, input().split())
S = input()
T = input()

prefix = T[:N]
sufix = T[::-1][:N]

if prefix == S:
    if sufix[::-1] == S:
        print(0)
    else:
        print(1)
elif sufix[::-1] == S:
    print(2)
else:
    print(3)
