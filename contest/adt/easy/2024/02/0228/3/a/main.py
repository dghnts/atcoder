A, B, C, D, E, F, X = map(int, input().split())

t = 0
a = 0

if X//(A+C) == 0:
    t = B*A
else:
    t = B*(A*X//(A+C) + X//(A+C))

if X//(D+F) == 0:
    a = E*D
else:
    a = E*(D*X//(D+F) + X//(D+F))

if a < t:
    print("Takahashi")
elif a > t:
    print("Aoki")
else:
    print("Draw")
