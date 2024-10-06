N = int(input())-1

even = ["0","2","4","6","8"]

num = []

while True:
    num.append(N%5)
    if N < 5:
        break
    N //= 5

num = num[::-1]

ans = [0 for _ in range(len(num))]

for i in range(len(num)):
    ans[i] = even[num[i]]

print("".join(ans))