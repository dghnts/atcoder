N = int(input())
A = [0]
'''
# N個のボタンについて光ったことがあるか判定
button = [False for _ in range(N)]
# 光っているボタンの番号
light = 1

for i in range(N):
    A.append(int(input()))

count = 0
while True:
    # 既に光ったことがあるボタンに戻ってきたら終了
    # print(light-1, button[light-1])
    if button[light-1]:
        print(-1)
        exit()
    else:
        button[light-1] = True
        light = A[light-1]
        count += 1
        if light == 2:
            print(count)
            exit()
'''

light = 1

for i in range(N):
    A.append(int(input()))

for j in range(1, N+1):
    light = A[light]
    if light == 2:
        print(j)
        exit()
print(-1)
