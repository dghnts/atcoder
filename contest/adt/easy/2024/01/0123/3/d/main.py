def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def is_convex(vertexes):
    flg = True
    for i in range(4):
        # 3頂点を時計回りに参照
        a = vertexes[i % 4]
        b = vertexes[(i + 1) % 4]
        c = vertexes[(i + 2) % 4]

        vec_ab = [b[0] - a[0], b[1] - a[1]]
        vec_bc = [c[0] - b[0], c[1] - b[1]]

        if cross(*vec_ab, *vec_bc) < 0:
            flg = False
            break

    # flg=True の場合は凸多角形、Falseは凸でない多角形
    return flg


print("OK")
vertexes = []

for i in range(4):
    vertexes.append(tuple(map(int, input().split())))

flag = is_convex(vertexes)

print("Yes" if flag else "No")
