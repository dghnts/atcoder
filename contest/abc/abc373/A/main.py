#!/usr/bin/env python3
import sys

# Generated by 2.14.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)


def main(S):
    count = 0
    for i, s in enumerate(S):
        if i+1 == len(s):
            count += 1
        else:
            continue
    print(count)
    return 0


S = []

for _ in range(12):
    S.append(input())


if __name__ == '__main__':
    main(S)
