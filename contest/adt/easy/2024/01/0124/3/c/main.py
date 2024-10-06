X = input()

if len(set(X)) == 1:
    print("Weak")
    exit()

for i in range(3):
    if int(X[i+1]) != (int(X[i])+1)%10:
        print("Strong")
        exit()

print("Weak")