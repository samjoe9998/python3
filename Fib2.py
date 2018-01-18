from itertools import islice


def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, curr+prev


f = fib()
result = list(islice(f, 0, 10))


print(result)


