import itertools

def all_variants(text):
    """
    Генератор обрубков.
    :param text: Строка str
    :yield: вариант обрубка поочередно
    """
    b = 1
    for i in range(len(text)+1):
        for j in range(len(text)+1-b):
            yield text[j:b+j]
        b += 1


a = all_variants("0123456789")

for i in a:
    print(i)
