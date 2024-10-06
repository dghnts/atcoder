Y = int(input())

mod4 = Y % 4
mod100 = Y % 100
mod400 = Y % 400

if mod4 != 0:
    ans = 365
else:
    if mod400 == 0:
        ans = 366
    elif mod100 == 0:
        ans = 365
    else:
        ans = 366
print(ans)
