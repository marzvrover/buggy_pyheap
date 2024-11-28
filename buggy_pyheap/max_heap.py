from .heap import Heap

class MaxHeap(Heap):
    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.storage[index] > self.get_parent(index):
            parent_index = self.get_parent_index(index)
            self.swap(parent_index, index)
            index = parent_index

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            larger_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.get_right_child(index) > self.get_left_child(index):
                larger_child_index = self.get_right_child_index(index)
            if self.storage[index] > self.storage[larger_child_index]:
                break
            self.swap(index, larger_child_index)
            index = larger_child_index
