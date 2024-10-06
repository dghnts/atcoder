x1, y1, x2, y2 = map(int, input().split())

vec = (x1-x2, y1-y2)
x3 = vec[1]+x2
y3 = -vec[0]+y2
x4 = vec[1]+x1
y4 = -vec[0]+y1

print(x3, y3, x4, y4)
