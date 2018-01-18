def something():
    result = []
    for x in range(10):
        result.append(x)
    return result


x = something()
print(x)


def something2():
    for x in range(10):
        yield x

y = list(something2())
print(y)


a = (x*x for x in range(10))
b = list(a);
print(b)

