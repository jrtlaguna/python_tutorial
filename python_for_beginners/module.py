

def helper():
    return print('This is module/method from the other side.')


def dec_test(func):
    def wrapper():
        print('This is a decorator.')

        return func()

    return wrapper
