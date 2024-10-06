from math import sin,cos,radians,pi,sqrt,isclose

def dist(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

S = list(input())
T = list(input())

vertexes_name = ["A","B","C","D","E"]
vertexes = {}

for i in range(5):
    rad = pi/2+2*i*pi/5
    vertexes[vertexes_name[i]] = tuple([sin(rad),cos(rad)])


if isclose(dist(vertexes[S[0]],vertexes[S[1]]),dist(vertexes[T[0]],vertexes[T[1]])):
    print("Yes")
else:
    print("No")
