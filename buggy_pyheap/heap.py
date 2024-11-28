from abc import ABC, abstractmethod

class Heap(ABC):
    def __init__(self):
        self.storage = []

    @property
    def size(self):
        return len(self.storage)

    @property
    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty:
            return None
        return self.storage[0]

    def pull(self):
        if self.is_empty:
            raise IndexError("Can't pull from empty heap")
        item = self.peek()
        if self.size == 1:
            return self.storage.pop()
        self.storage[0] = self.storage.pop()
        self.heapify_down()
        return item

    def add(self, elem):
        self.storage.append(elem)
        self.heapify_up()

    @abstractmethod
    def heapify_up(self):
        pass

    @abstractmethod
    def heapify_down(self):
        pass

    @staticmethod
    def get_left_child_index(parent):
        return (2 * parent) + 1

    @staticmethod
    def get_right_child_index(parent):
        return (2 * parent) + 2

    @staticmethod
    def get_parent_index(child):
        return (child - 1) // 2

    def has_left_child(self, parent):
        return self.get_left_child_index(parent) < self.size

    def has_right_child(self, parent):
        return self.get_right_child_index(parent) < self.size

    def has_parent(self, child):
        return child != 0 and self.get_parent_index(child) >= 0

    def get_left_child(self, parent):
        return self.storage[self.get_left_child_index(parent)]

    def get_right_child(self, parent):
        return self.storage[self.get_right_child_index(parent)]

    def get_parent(self, child):
        return self.storage[self.get_parent_index(child)]

    def swap(self, first, second):
        self.storage[first], self.storage[second] = self.storage[first], self.storage[second]
