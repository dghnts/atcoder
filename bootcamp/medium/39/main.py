K, A, B = map(int, input().split())

'''
# 1円で交換するビスケットの枚数< 1円と交換するビスケットの枚数ならビスケットを増やし続けるl
if B < A:
    bis = K+1
else:
    bis = K+1
    K -= A-1
    bis = max(bis, A+(B-A)*(K//2)+K % 2)

print(bis)
'''

if B-A <= 2:
    print(K+1)
else:
    bis = A
    K -= A-1
    if K % 2 == 1:
        bis += 1
        K -= 1
    bis += K//2*(B-A)
    print(bis)
