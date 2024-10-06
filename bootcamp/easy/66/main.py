S = input()

dict = {"N": 0, "E": 0, "S": 0, "W": 0}
for s in S:
    dict[s] += 1

flag = True
if dict["N"] != 0:
    if dict["S"] == 0:
        flag = False

if dict["S"] != 0:
    if dict["N"] == 0:
        flag = False

if dict["E"] != 0:
    if dict["W"] == 0:
        flag = False

if dict["W"] != 0:
    if dict["E"] == 0:
        flag = False

print("Yes" if flag else "No")
