S = []

for i in range(10):
    S.append(input())
    
A,B,C,D = 0,0,0,0

for i in range(10):
    if "#" in S[i]:
        if A == 0:
            A = i+1
        B = max(B,i+1)            
        for j in range(10):
            if S[i][j] == "#":
                if C == 0:
                    C = j+1
                D = max(D,j+1)

print(A,B)
print(C,D)