class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty queue.")
        value = self.front.value
        self.front = self.front.next
        self.size -= 1
        return value

    def size_of(self):
        return self.size

#    def display(self):
#        current = self.front
#        while current:
#            print(current.value, "--->", end='')
#            current = current.next



