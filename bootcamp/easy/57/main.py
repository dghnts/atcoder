import math
A, B = map(int, input().split())

for i in range(5000):
    tax_eight = i*0.08
    tax_ten = i*0.1
    if math.floor(tax_eight) == A and math.floor(tax_ten) == B:
        print(i)
        exit()
print(-1)
