N = int(input())
print("Yes" if abs(N) < 2**31 or N == -1*2**31 else "No")
