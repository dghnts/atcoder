A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

mod = [(10-A % 10) % 10, (10-B % 10) % 10, (10-C % 10) %
       10, (10-D % 10) % 10, (10-E % 10) % 10]
mod.sort()

ans = A+B+C+D+E
print(ans+sum(mod[:-1]))
