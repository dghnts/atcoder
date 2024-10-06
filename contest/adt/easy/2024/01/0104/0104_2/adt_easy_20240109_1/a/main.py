V, A, B, C = map(int, input().split())


if V // (A + B + C) != 0:
    V = V % (A + B + C)

if V - A < 0:
    print("F")
    exit()

V -= A

if V - B < 0:
    print("M")
    exit()

V -= B

print("T")
