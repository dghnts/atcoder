Q, H, S, D = map(int, input().split())
N = int(input())

n = N//2
r = N % 2

print(n*min(8*Q, min(4*H, min(2*S, D)))+min(4*Q, min(2*H, S))*r)
