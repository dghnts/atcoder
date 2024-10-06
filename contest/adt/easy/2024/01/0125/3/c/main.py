N,X,Y,Z=map(int,input().split())
A = {i+1:int(x) for i,x in enumerate(input().split())}
B = {i+1:int(x) for i,x in enumerate(input().split())}
C = {}

for i in range(1,N+1):
    C[i] = A[i]+B[i]


A = sorted(A.items(),reverse=True,key=lambda x:x[1])
B = sorted(B.items(),reverse=True,key=lambda x:x[1])
C = sorted(C.items(),reverse=True,key=lambda x:x[1])

ans = []
count = 0
for a in A:
    if count == X:
        count = 0
        break
    ans.append(a[0])
    count+=1
    
for b in B:
    if count == Y:
        count = 0
        break
    if not b[0] in ans:
        ans.append(b[0])
        count += 1

for c in C:
    if count == Z:
        count = 0
        break
    if not c[0] in ans:
        ans.append(c[0])
        count += 1

ans = sorted(list(set(ans)))
for i in ans:
    print(i)