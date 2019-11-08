# Counting bits
def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

# Checking parity
def parityBF(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

def parityTrick(x):
    result = 0
    while x:
        result ^= 1
        x &= x-1
    return result
