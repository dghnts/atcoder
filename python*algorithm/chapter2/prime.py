N = int(input())
# N-1までの数が素数か判定するフラグを設定
p = [True]*N

# 0と1は素数ではない
p[0] = False
p[1] = True

# 2からチェックしていく
n = 2


def hyou():
    s = ""
    for i in range(N):
        if p[i]:
            s += str(i).zfill(2)+", "
            # s += {:2d}, ".format(i)
        else:
            s += "/, "
        # 1の位が9のとき改行を追加
        if i % 10 == 9:
            s += "\n"
    print(s)


def furui():
    global n
    global N
    # n刻みで数をチェックする
    for i in range(n+n, N, n):
        p[i] = False
    print(n, "の倍数を篩い落としました")
    hyou()
    while n < N:
        n += 1
        if p[n]:
            break


hyou()
while n*n < N:
    input("Enterキーをおしてください")
    furui()
