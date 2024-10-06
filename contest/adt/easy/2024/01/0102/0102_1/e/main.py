S = input()

ans = 0

while True:
    if S == 0:
        break
    S.rstrip()
    if S[-1] == "0":
        S.rstrip()
        
print(ans)