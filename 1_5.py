def compression(s):
    N = len(s)
    if (N <= 2): return s
    Now = s[0]
    Compressed = []
    Counter = 0
    for letter in s:
        if (letter == Now): Counter += 1
        else:
            Compressed += [Now,str(Counter)]
            Now = letter
            Counter = 1
    Compressed += [Now,str(Counter)]
    if (len(Compressed) < N): return "".join(Compressed)
    else: return s

test_dict = {
    "Abcd" : "Abcd",
    "AAAbcd" : "AAAbcd",
    "Abcdeeeeeeee": "A1b1c1d1e8",
    "" : ""
}

for test, result in test_dict.items():
    print(f"For {test} answer is {compression(test) == result}")
