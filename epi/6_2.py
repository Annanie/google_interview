def reverse_words(s):
    # First, reverse the whole string.
    s .reverse()
    def reverse_range(s, start, end):
        while start < end:
        s[start], s[end] = s[end], s[start]
        start, end = start + 1, end - 1
        start = 0
    while True:
    end = s.find(b' ', start)
    if end < 0:
    break
    # Reverses each word in the string.
    reverse_range(s, start, end - 1)
    start = end + 1
    # Reverses the last word.
    reverse_range(s, start, len(s) - 1)
