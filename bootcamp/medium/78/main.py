s = list(input())
k = int(input())

res = 0
i = 1

seq = s[0]
seqs = []
while i < len(s):
    if s[i-1] == s[i]:
        seq += s[i]
    else:
        res += len(seq)//2
        if seq != []:
            seqs.append(seq)
        seq = s[i]
    if i == len(s)-1:
        res += len(seq)//2
        if seq != []:
            seqs.append(seq)
    i += 1

res *= k

if s[0] == s[-1]:
    res -= (int(len(seqs[0])/2)+int(len(seqs[-1])/2) -
            int((len(seqs[0])+len(seqs[-1]))/2))*(k-1)

print(res)
