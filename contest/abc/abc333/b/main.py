S = input()
T = input()
S = {S[:1], S[1:]}
T = {T[:1], T[1:]}

dist1 = [{"A", "B"}, {"B", "C"}, {"C", "D"}, {"D", "E"}, {"E", "A"}]
dist2 = [{"A", "C"}, {"A", "D"}, {"B", "D"}, {"B", "E"}, {"C", "E"}]

if S in dist1 and T in dist1:
    print("Yes")
elif S in dist2 and T in dist2:
    print("Yes")
else:
    print("No")
