s = {}
s["a"] = list(input())[::-1]
s["b"] = list(input())[::-1]
s["c"] = list(input())[::-1]

person = "a"

while True:
    if len(s[person]) == 0:
        break
    # print(person, s[person])
    person = s[person].pop()
    # print(person)

print(person.upper())
