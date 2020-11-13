def even_iter_impl(iterable):
    while True:
        # PEP 479
        try:
            yield next(iterable)
            next(iterable)
        except StopIteration:
            return


class even_iter:

    def __init__(self, iterable):
        self.iter = iter(iterable)

    def __iter__(self):
        yield from even_iter_impl(self.iter)


a = [i for i in range(0, 10)]

print(a)
print([i for i in iter(a)])
print(iter(even_iter(a)))
print([i for i in even_iter(a)])
