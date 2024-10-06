x1, y1, x2, y2 = map(int, input().split())

a = [x1, y1]
b = [x2, y2]

# aとの距離が√5であるこうしをれっきょしてbとの距離を考える
vec = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

for i in range(8):
    c = [a[0]+vec[i][0], a[1]+vec[i][1]]
    # print(a)
    if [c[0]-b[0], c[1]-b[1]] in vec:
        print("Yes")
        exit()
print("No")
