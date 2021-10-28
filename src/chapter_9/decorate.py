def decorate(func):
    print('in decorate function, decorating', func.__name__)

    def wrapper_func(*args):
        print('Executing', func.__name__)
        return func(*args)

    return wrapper_func


def myfunction(parameter):
    print(parameter)


myfunction = decorate(myfunction)
print(myfunction('hello'))


@decorate
def otherfunction(parameter):
    print(parameter)


print(otherfunction('hello'))
