import pytest
import random
import sys

from buggy_pyheap.min_heap import MinHeap

MIN_INT = -sys.maxsize - 1
MAX_INT = sys.maxsize

def test_size():
    heap = MinHeap()
    assert heap.size == 0
    heap.add(1)
    assert heap.size == 1
    heap.add(2)
    assert heap.size == 2

def test_is_empty():
    heap = MinHeap()
    assert heap.is_empty
    heap.add(1)
    assert not heap.is_empty

def test_peek():
    heap = MinHeap()
    assert heap.peek() is None
    heap.add(1)
    assert heap.peek() == 1
    heap.add(2)
    assert heap.peek() == 1

def test_pull():
    heap = MinHeap()
    with pytest.raises(IndexError):
        heap.pull()
    heap.add(1)
    assert heap.pull() == 1
    with pytest.raises(IndexError):
        heap.pull()
    heap.add(2)
    heap.add(1)
    assert heap.pull() == 1
    assert heap.pull() == 2

def test_add():
    heap = MinHeap()
    heap.add(1)
    assert heap.size == 1
    assert heap.peek() == 1
    heap.add(2)
    assert heap.size == 2
    assert heap.peek() == 1
    heap.add(0)
    assert heap.size == 3
    assert heap.peek() == 0

def test_heapify_up():
    heap = MinHeap()
    heap.add(3)
    heap.add(1)
    heap.add(2)
    assert heap.storage == [1, 3, 2]

def test_heapify_down():
    heap = MinHeap()
    heap.add(10)
    heap.add(20)
    heap.add(15)
    heap.add(30)
    heap.add(40)
    heap.add(50)
    heap.add(5)
    heap.add(1)
    heap.pull()
    assert heap.storage == [5, 20, 10, 30, 40, 50, 15]
    heap.pull()
    assert heap.storage == [10, 20, 15, 30, 40, 50]
    heap.pull()
    assert heap.storage == [15, 20, 50, 30, 40]

def test_min_heap_basic():
    heap = MinHeap()
    heap.add(3)
    heap.add(1)
    heap.add(2)
    assert heap.pull() == 1
    assert heap.pull() == 2
    assert heap.pull() == 3
    with pytest.raises(IndexError):
        heap.pull()

def test_min_heap_in_depth():
    number_of_heaps = 1000
    max_number_of_values = 1000

    for _ in range(number_of_heaps):
        values = []
        heap = MinHeap()

        amount = random.randint(1, max_number_of_values)
        for _ in range(amount):
            value = random.randint(MIN_INT, MAX_INT)
            values.append(value)
            heap.add(value)

        values.sort(reverse=False)

        for value in values:
            assert value == heap.pull()
