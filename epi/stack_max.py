from collections import namedtuple

class StackCached:                                        # trzymam cached poprzednie maxy

    ElWithMax = nt('ElWithMax', 'Element max')

    def __init__(self, ):
        self._CachedMax = []

    def empty(stack):
        return len(self.ElWithMax) == 0

    def max(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        else:
            return self._CachedMax[-1]

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._CachedMax.pop().Element

    def push(self, val):
        self._CachedMax.append(
            self.ElWithMax(x, x if self.empty() else max(
                x, self.max())
            )
        )
