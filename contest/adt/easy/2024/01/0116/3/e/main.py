from collections import defaultdict
N, Q = map(int, input().split())

follow = defaultdict(set)

for i in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if not B in follow[A]:
            follow[A].add(B)
    if T == 2:
        if B in follow[A]:
            follow[A].remove(B)
    if T == 3:
        if B in follow[A] and A in follow[B]:
            print("Yes")
        else:
            print("No")