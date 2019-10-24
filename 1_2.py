def reverse(s):
    l = list(s)
    for i in range(int(len(l)/2)):
        tmp = l[i]
        l[i] = l[-(i+1)]
        l[-(i+1)] = tmp
    return "".join(l)

test_dict = {
    "abcd": "dcba",
    "abc": "cba",
    "":""
}

for test, result in test_dict.items():
    print(f"For '{test}' result is {result == reverse(test)}")
