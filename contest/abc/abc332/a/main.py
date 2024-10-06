N, S, K = map(int, input().split())

product_price = 0
send_price = 0
for i in range(N):
    P, Q = map(int, input().split())
    product_price += P*Q

if product_price < S:
    send_price = K

print(product_price+send_price)
