corrects = ["and", "not", "that", "the", "you"]

N = int(input())
W = set(input().split())

for w in W:
    if w in corrects:
        print("Yes")
        exit()
print("No")