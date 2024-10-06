N,K = map(int,input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

eats = set()

for i,a in enumerate(A):
    if a == max(A):
        eats.add(i+1)

for b in B:
    if b in eats:
        print("Yes")
        exit()
print("No")