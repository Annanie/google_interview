def freq_dict(s):
    D = {}
    for letter in s:
        if letter not in D.keys(): D[letter] = 1
        else: D[letter] += 1
    return D

def compare(s1,s2):
    if len(s1) != len(s2): return False
    D1 = freq_dict(s1)
    for letter in s2:
        if letter not in D1 or D1[letter] == 0: return False
        D1[letter] -= 1
    return True

test_list = [
    ["abc", "abc"],
    ["cba", "acb"],
    ["adc", "abc"],
    ["234a", "sd"]
]

for test in test_list:
    print(f"For test '{test[0]}' and '{test[1]}' answer is {compare(test[0],test[1])}")
