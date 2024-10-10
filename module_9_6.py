import itertools

def all_variants(text):
    """
    Генератор обрубков.
    :param text: Строка str
    :yield: вариант обрубка поочередно
    """
    a, b = 0, 1
    for i in range(len(text)+1):
        for j in range(len(text)+1-b):
            yield text[a+j:b+j]
        b += 1





a = all_variants("abcdef")

for i in a:
    print(i)
