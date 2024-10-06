N, A, B = map(int, input().split())
S = input()
Pass_a = 0
Pass_b = 0

for s in S:
    if s == "c":
        print("No")
    elif s == "a":
        if Pass_a + Pass_b < A+B:
            print("Yes")
            Pass_a += 1
        else:
            print("No")
    else:
        if Pass_a + Pass_b < A+B and Pass_b < B:
            print("Yes")
            Pass_b += 1
        else:
            print("No")
        