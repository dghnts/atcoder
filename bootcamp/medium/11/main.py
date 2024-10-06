N, M = map(int, input().split())

students = []

for i in range(N):
    students.append(tuple([int(x) for x in input().split()]))

checkpoints = [(float("inf"), float("inf"))]

for j in range(M):
    checkpoints.append(tuple([int(x) for x in input().split()]))

for student in students:
    dist = float('inf')
    goal = 0
    for j in range(1, M+1):
        new_dist = abs(student[0]-checkpoints[j][0]) + \
            abs(student[1]-checkpoints[j][1])
        if new_dist < dist:
            dist = new_dist
            goal = j
    print(goal)
