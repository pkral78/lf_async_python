class even_iter:

    def __init__(self, iterable):
        self.iter = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        ret = next(self.iter)
        try:
            next(self.iter)
        except StopIteration:
            pass
        return ret


a = [i for i in range(0, 10)]

print(a)
print([i for i in iter(a)])
print(iter(even_iter(a)))
print([i for i in even_iter(a)])
