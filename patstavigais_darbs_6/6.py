class MyRange:

    def __init__(self, stop, start=0, step=1):
        self.current = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        return self

    def __next__(self):
        can_next = (self.step > 0 and self.current < self.stop) \
            or (self.step < 0 and self.current > self.stop)

        if can_next:
            result = self.current
            self.current += self.step

            return result
        else:
            raise StopIteration
