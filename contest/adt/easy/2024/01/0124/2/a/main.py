ans = tuple()
x_coords = []
y_coords = []

for i in range(3):
    x,y = tuple(map(int,input().split()))
    x_coords.append(x)
    y_coords.append(y)

ans = [0,0]
for x in x_coords:
    if x_coords.count(x) == 1:
        ans[0] = x
            
for y in y_coords:
    if y_coords.count(y) == 1:
        ans[1] = y    

print(*ans)