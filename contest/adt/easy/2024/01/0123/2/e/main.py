N,M=map(int,input().split())
S = input()

normal = M
logo = 0
used_logo = 0
for i in range(N):
    if S[i] == "0":
        normal = M
        used_logo = 0
    elif S[i] == "1" and normal != 0:
            normal -= 1
    elif used_logo != logo:
            used_logo += 1
    else:
        logo += 1
        used_logo += 1

print(logo)