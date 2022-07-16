class CyclesQueueListItem:
    def __init__(self, next_element=None):
        self._data = 0
        self._next_element = next_element

    @property
    def next_element(self):
        return self._next_element

    @next_element.setter
    def next_element(self, next_element):
        self._next_element = next_element

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data


class Queue2:
    def __init__(self, size):
        self._size = size
        self._count = 0

        temp = CyclesQueueListItem()
        first = temp

        for i in range(size - 1):
            temp = CyclesQueueListItem(temp)

        first.next_element = temp

        self._head = first
        self._tail = first

    def size(self):
        return self._size

    def count(self):
        return self._count

    def append(self, el):
        if self._count == self._size:
            raise Exception("Queue is full!")

        self._head.data = el
        self._count += 1
        self._head = self._head.next_element

    def pop(self):
        if self._count == 0:
            raise Exception("Queue is empty!")

        item = self._tail.data

        self._count -= 1

        self._tail = self._tail.next_element
        return item


q = Queue2(3)
q.append(3)
q.append(2)
print(q.size())
