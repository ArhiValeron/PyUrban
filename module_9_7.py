try:
    from sympy.ntheory import isprime
except ModuleNotFoundError:
    import sys
    import subprocess
    print("Модуль sympy не установлен. Установка...")
    subprocess.run([sys.executable, "-m", "pip", "install", "sympy"])
    print("Установка завершена.")
    from sympy.ntheory import isprime

def is_prime_(func):
    """
    Декоратор, который обьединяет две функции сложение и проверку простое ли число.
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isprime(result):
            print("Простое")
            return result
        else:
            print("Составное")
            return result

    return wrapper


@is_prime_
def sum_three(a, b, c):
    """
    Складывает три числа.
    """
    return a + b + c


result = sum_three(2 ** 31, 1, 0)
print(result)
result = sum_three(2 ** 127, -1, 0)
print(result)
