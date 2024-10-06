a, b = map(int, input().split())


print("Yes" if abs(a % 10 - b % 10) == 1 or abs(a % 10 - b % 10) == 9 else "No")
