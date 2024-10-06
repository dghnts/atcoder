import math
A, B, C, D = map(int, input().split())

divide_C = B//C-(A+C-1)//C+1
divide_D = B//D-math.ceil(A/D)+1
lcm = C*D//math.gcd(C, D)
divide_CD = B//lcm-math.ceil(A/lcm)+1
total = B-A+1
# print(total)
# print(divide_C)
# print(divide_D)
# print(divide_CD)
print(total-(divide_C+divide_D-divide_CD))
