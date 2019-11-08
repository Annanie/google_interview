def int_to_str(x):
    neg = False
    if x < 0:
        x, neg = -x, True

    s = []
    if x == 0: return "0"
    while x != 0:
        s.append(chr(ord('0') + x % 10))
        x //= 10

    return ('-' if neg else '') + ''.join(reversed(s))

def str_to_int(s):
    neg_mul = 1
    ind = 0
    if s[0] == '-':
        ind, neg_mul = 1, -1
    num = 0
    pow = 1
    for i in range(len(s) - ind):
        num += (ord(s[~i]) - ord('0'))*pow
        pow *= 10
    return neg_mul * num


test_dict = {
    123: "123",
    -123: "-123",
    0: "0",
}

for int, str in test_dict.items():
    print(f"For int_to_str {int} result is {int_to_str(int) == str}")
    print(f"For str_to_int {str} result is {str_to_int(str) == int}")
