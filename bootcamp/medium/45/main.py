num_s, num_c = map(int, input().split())

if 2*num_s <= num_c:
    ans = num_s + (num_c-2*num_s)//4
else:
    ans = num_c//2

print(ans)
