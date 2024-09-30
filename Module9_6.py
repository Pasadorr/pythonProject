def all_variants(text):
    length = len(text)
    for begin in range(length):
        for stop in range(begin + 1, length + 1):
            yield text[begin:stop]

a = all_variants("abc")
for list_ in a:
    print(list_)