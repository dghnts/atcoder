X = int(input())

if X >= 90:
    print("expert")
    exit()
if X >= 70:
    print(90-X)
    exit()
if X >= 40:
    print(70-X)
    exit()
print(40-X)