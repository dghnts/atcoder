N, K = map(int, input().split())

N -= N//K * K

print(min(N, abs(N-K)))
