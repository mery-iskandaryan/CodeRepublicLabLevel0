class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def is_empty(self):
        return self.size == 0

    def size_of(self):
        return self.size()

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        remove = self.top.value
        self.top = self.top.next
        self.size -= 1
        return remove






