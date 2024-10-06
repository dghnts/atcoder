A, B, C, D = map(int, list(input()))

op = ["-", "+"]

for op1 in op:
    for op2 in op:
        for op3 in op:
            ans = A
            if op1 == "+":
                ans += B
            else:
                ans -= B
            if op2 == "+":
                ans += C
            else:
                ans -= C
            if op3 == "+":
                ans += D
            else:
                ans -= D
            # print(ans)
            if ans == 7:
                print("%d%s%d%s%d%s%d=7" % (A, op1, B, op2, C, op3, D))
                exit()
            # print(op1, op2, op3)
