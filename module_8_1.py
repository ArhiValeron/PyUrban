def add_everything_up(arg1, arg2):
    try:
        z = arg1 + arg2
    except:
        z = str(arg1) + str(arg2)
    finally:
        return z

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
