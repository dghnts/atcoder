N = int(input())
# Nまでの素数を判定する


def furui():
    global N
    flag = [True] * (N+1)
    # 0と1は素数ではない
    flag[0] = False
    flag[1] = False

    # チェックする最初の数を指定
    m = 2

    while m*m < N:
        for i in range(2*m, N+1, m):
            flag[i] = False

        m += 1

        while not flag[m]:
            m += 1

    prime = []
    for i in range(N+1):
        if flag[i]:
            prime.append(i)
    return prime


print(furui())
