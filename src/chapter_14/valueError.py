class ValueTooLarge(Exception):
    pass


def test(x):
    if x > 1000:
        raise ValueTooLarge(f'"x" is too large ("x" = {x})')
    else:
        return x


print(test(353))
print(test(2000))
