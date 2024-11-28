import pytest
import random
import sys

from buggy_pyheap.max_heap import MaxHeap

MIN_INT = -sys.maxsize - 1
MAX_INT = sys.maxsize

def test_size():
    heap = MaxHeap()
    assert heap.size == 0
    heap.add(1)
    assert heap.size == 1
    heap.add(2)
    assert heap.size == 2

def test_is_empty():
    heap = MaxHeap()
    assert heap.is_empty
    heap.add(1)
    assert not heap.is_empty

def test_peek():
    heap = MaxHeap()
    assert heap.peek() is None
    heap.add(1)
    assert heap.peek() == 1
    heap.add(2)
    assert heap.peek() == 2

def test_pull():
    heap = MaxHeap()
    with pytest.raises(IndexError):
        heap.pull()
    heap.add(1)
    assert heap.pull() == 1
    with pytest.raises(IndexError):
        heap.pull()
    heap.add(2)
    heap.add(1)
    assert heap.pull() == 2
    assert heap.pull() == 1

def test_heapify_up():
    heap = MaxHeap()
    heap.add(3)
    heap.add(1)
    heap.add(2)
    assert heap.storage == [3, 1, 2]

def test_heapify_down():
    heap = MaxHeap()
    heap.add(100)
    heap.add(90)
    heap.add(80)
    heap.add(70)
    heap.add(60)
    heap.add(50)
    heap.add(40)
    heap.add(30)
    heap.pull()
    assert heap.storage == [90, 70, 80, 30, 60, 50, 40]
    heap.pull()
    assert heap.storage == [80, 70, 50, 30, 60, 40]
    heap.pull()
    assert heap.storage == [70, 60, 50, 30, 40]

def test_max_heap():
    heap = MaxHeap()
    heap.add(3)
    heap.add(1)
    heap.add(2)
    assert heap.pull() == 3
    assert heap.pull() == 2
    assert heap.pull() == 1
    with pytest.raises(IndexError):
        heap.pull()

def test_max_heap_in_depth():
    number_of_heaps = 1000
    max_number_of_values = 1000

    for _ in range(number_of_heaps):
        values = []
        heap = MaxHeap()

        amount = random.randint(1, max_number_of_values)
        for _ in range(amount):
            value = random.randint(MIN_INT, MAX_INT)
            values.append(value)
            heap.add(value)

        values.sort(reverse=True)

        for value in values:
            assert value == heap.pull()
