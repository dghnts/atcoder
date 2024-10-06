N = input()

if int(N) > 41:
    N = str(int(N)+1)

print("AGC"+N.zfill(3))