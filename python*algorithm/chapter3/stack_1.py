N = int(input())
stack = [0]*N
sp = 0  # スタックポインタ //データの出し入れの位置を管理


def push(d):
    # global N
    global sp
    if sp < N:
        stack[sp] = d
        sp += 1
        print("データ", d, "を追加しました")
    else:
        print("これ以上データを入れられません")


def pop():
    global sp
    if sp > 0:
        sp -= 1
        return stack[sp]
    else:
        print("取り出すデータが存在しません")
        return None


for i in range(N+1):
    push(i)
for i in range(N+1):
    d = pop()
    print("取り出したデータ", d)
