N = int(input())
T = list(input())

x = 0
y = 0

directions = ["east", "south", "west", "north"]
direction = "east"

for t in T:
    if t == "S":
        if direction  == "east":
            x += 1
        elif direction == "south":
            y -= 1
        elif direction == "west":
            x -= 1
        else:
            y += 1
    else:
        direction = directions[(directions.index(direction)+1)%4]
#    print(x,y)
print(x,y)