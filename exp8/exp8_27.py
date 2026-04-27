class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end     = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

for n in CountUp(1, 5):
    print(n, end=" ")
# 1 2 3 4 5