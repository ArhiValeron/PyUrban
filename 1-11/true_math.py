from math import inf

def divide(first,second):
    try:
        answer = first/second
    except:
        answer = inf
    finally:
        return answer

