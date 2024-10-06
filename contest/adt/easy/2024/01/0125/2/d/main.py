K,G,M = map(int,input().split())

glass = 0
cup = 0

for i in range(K):
    if glass == G:
        glass = 0
    elif cup == 0:
        cup = M
    elif G-glass <= cup:
        cup -= G-glass
        glass = G
    else:
        glass += cup
        cup = 0
    #print(glass,cup)
    
print(glass,cup)