a, b = input().split()
chk = int(a+b)

for i in range(1000):
    if i**2 == chk:
        print("Yes")
        exit()
print("No")
