N = int(input())
A = [int(x) for x in input().split()]

max_a = max(A)
score = 0
ans = 0
for i,a in enumerate(A):
    if a != max_a:
        if score < a:
            score = a
            ans = i+1

print(ans)