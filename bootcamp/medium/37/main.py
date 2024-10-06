N = int(input())
h = [int(h) for h in input().split()]

ans = 0

count = 0
while True:
    # hの全ての値が0になるまで繰替える
    if max(h) == 0:
        break
    i = 0
    while i < N:
        # h[i]が0ならh[i+1]の確認にうつる
        if h[i] == 0:
            i += 1
        else:
            ans += 1
            while i < N and h[i] > 0:
                h[i] -= 1
                i += 1

print(ans)
