class CyclesQueue:
    def __init__(self, size):
        self._items = [0] * size
        self._head = 0
        self._tail = 0
        self._count = 0
        self._size = size

    def append(self, el):
        if self._size == self._count:
            raise Exception("Queue is full!")

        self._items[self._head] = el
        self._count += 1
        self._head = self.next_index(self._head)

    def pop(self):
        if self._count == 0:
            raise Exception("Queue is empty!")

        item = self._items[self._tail]

        self._count -= 1

        self._tail = self.next_index(self._tail)
        return item

    def count(self):
        return self._count

    def size(self):
        return self._size

    def clear(self):
        self._items = []

    def next_index(self, index):
        temp = index + 1
        if temp >= self._size:
            temp = 0
        return temp

    def print_items(self):
        return self._items


q = CyclesQueue(5)
q.append(2)
q.append(5)
q.append(10)
print(q.print_items())
q.clear()
print(q.print_items())
