X, Y = map(int, input().split())

if (X < Y and Y <= X + 2):
    print("Yes")
elif(Y < X and Y >= X - 3):
    print("Yes")
else:
    print("No")
