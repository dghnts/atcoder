K, G, M = map(int, input().split())

glass = 0
magcup = 0

for i in range(K):
    if glass == G:
        glass = 0
    elif magcup == 0:
        magcup = M
    else:
        mag_to_glass = G - glass
        if magcup > mag_to_glass:
            glass += mag_to_glass
            magcup -= mag_to_glass
        else:
            glass += magcup
            magcup = 0

print(glass, magcup)
