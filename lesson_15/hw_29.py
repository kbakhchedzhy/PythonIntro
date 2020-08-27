
class Counter:
    current = 0

    def __init__(self, min_v, max_v):
        self.min_v = min_v
        self.max_v = max_v

    def count(self):
        if not self.current:
            self.current = self.min_v
        if self.current <= self.max_v - 1:
            self.current += 1
            return self.current


cnt = Counter(0, 100)
for _ in range(cnt.min_v, cnt.max_v):
    print(cnt.count())
