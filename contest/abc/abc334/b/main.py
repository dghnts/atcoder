A, M, L, R = map(int,input().split())

#Aを原点とする相対座標に変換
L -= A
R -= A

L += (M-L % M) % M
R -= R % M

print((R-L)//M + 1)