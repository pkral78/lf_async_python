class skip_iter:

    def __init__(self, iterable):
        self.iter = iter(iterable)

    def __iter__(self):
        last = 0
        while True:
            # PEP 479
            try:
                skip = (yield next(self.iter)) or last
                last = skip
                for i in range(0, skip):
                    next(self.iter)
            except StopIteration:
                return


a = [i for i in range(0, 10)]

print(a)
print([i for i in iter(a)])
print(iter(skip_iter(a)))
print([i for i in skip_iter(a)])

it = iter(skip_iter(a))
print(next(it))
print(it.send(2))
print(next(it))
