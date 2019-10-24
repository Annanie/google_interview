def findUnique(s):
    if len(s) < 2:
        return True
    D = {s[0]:1}
    for letter in s[1:]:
        if letter in D: return False
        D[letter] = 1
    return True

test_strings = [
    "themy",                # general good
    "gratsr",               # general bad
    ""                      # null edge case
]

for test in test_strings:
    print(f"{test} => {findUnique(test)}")
