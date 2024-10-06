S = input()

ans = 753

for i in range(len(S)-2):
    if ans > abs(int(S[i:i+3])-753):
        # print(ans)
        ans = abs(753-int(S[i:i+3]))
print(ans)
