#!/usr/bin/env python3
from string import ascii_uppercase


def solve(D: dict):
    dist = 0
    a = D["A"]
    for s in ascii_uppercase[1:]:
        b = D[s]
        dist += abs(b-a)
        a = b
    return dist


def main():
    def set_position(pos={upper: 0 for upper in ascii_uppercase}):
        S = input()
        for i, s in enumerate(S):
            pos[s] = i+1
        return pos
    position = set_position()
    print(solve(position))


if __name__ == '__main__':
    main()
