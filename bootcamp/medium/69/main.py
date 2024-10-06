n = int(input())

ride = [0]*5

for i in range(5):
    ride[i] = int(input())

print((n+min(ride)-1)//min(ride)+4)
