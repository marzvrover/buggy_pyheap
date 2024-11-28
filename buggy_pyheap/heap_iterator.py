class HeapIterator:
    def __init__(self, heap):
        self.heap = heap

    def __iter__(self):
        return self

    def __next__(self):
        if self.heap.is_empty:
            raise StopIteration
        return self.heap.pull()
