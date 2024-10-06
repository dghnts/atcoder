def is_prime(N):
    if N <= 1:
        return False
    i = 2
    while i*i < N:
        if N % i == 0:
            return False
        i += 1
    return True


X = int(input())

ans = X
'''
flag = False
while True:
    if flag:
        break
    i = 2
    while True:
        if i*i > X:
            flag = True
            break
        elif X % i == 0:
            X += 1
            break
        else:
            i += 1
print(X)
'''

while not is_prime(ans):
    ans += 1

print(ans)
