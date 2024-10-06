from collections import defaultdict

N, T = map(int, input().split())

points_list = [0 for _ in range(N)]

points_dict = defaultdict(int)
points_dict[0] = N

variety = 1

for i in range(T):
    person, point = map(int, input().split())
    current_point = points_list[person-1]
    points_dict[current_point] -= 1
    if points_dict[current_point] == 0:
        variety -= 1
    new_point = current_point + point
    points_list[person-1] = new_point
    points_dict[new_point] += 1
    if points_dict[new_point] == 1:
        variety += 1
    print(variety)
