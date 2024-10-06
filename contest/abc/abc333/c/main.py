N = int(input())

num1 = str(1)
num2 = str(1)
num3 = str(1)
count = 0

for i in range(N-1):
    if num1 != num2:
        if num2 != num3:
            num3 = str(1)+num3
        else:
            num2 = str(1)+num2
            num3 = str(1)
    elif num3 != num1:
        num3 = str(1)+num3
    else:
        num1 = str(1)+num1
        num2 = str(1)
        num3 = str(1)

#print(num1, num2, num3)
print(int(num1)+int(num2)+int(num3))
