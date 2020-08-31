
class Counter:

    def __init__(self, min_v, max_v):
        self.min_v = min_v
        self.max_v = max_v
        self.current = min_v

    def count(self):
        if self.current == self.min_v:
            print(self.current)

        if self.current <= self.max_v - 1:
            self.current += 1
            return self.current


cnt = Counter(-2, 100)
for _ in range(cnt.min_v, cnt.max_v):
    print(cnt.count())
