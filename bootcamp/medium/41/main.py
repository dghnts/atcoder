from string import ascii_lowercase

alph = ascii_lowercase
S = input()


def shrink(s, S):
    count = 0
    string = S
    while True:
        if len(string) == 1 or len(set(string)) == 1:
            return count

        new_string = ""
        for i in range(len(string) - 1):
            if string[i] == s or string[i + 1] == s:
                new_string += s
            else:
                new_string += string[i]
        else:
            count += 1
            # print(string, "->", new_string)
            string = new_string


def main():
    ans = len(S)
    for s in alph:
        ans = min(shrink(s, S), ans)
        # print(ans)
    return print(ans)


if __name__ == "__main__":
    main()
