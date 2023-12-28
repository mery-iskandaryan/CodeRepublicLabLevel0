class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __eq__(self, other):
        return self.data == other.data


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return not self.head

    def append(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def prepend(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def clear(self):
        self.head = None

    def get_size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next
        return size

    def delete(self, data):
        current = self.head
        while current.next:
            if self.head.data == data:
                self.head = self.head.next
                break
            if current.next.data == data:
                current.next = current.next.next
                break
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data} --> ", end='')
            current = current.next

    def insert_after(self, node, data_to_insert):
        current = self.head
        node_to_insert = Node(data_to_insert)
        while current.data != node.data:
            current = current.next
        tmp = current.next
        current.next = node_to_insert
        node_to_insert.next = tmp


a = LinkedList()
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.prepend(1)
n = Node(3)
a.insert_after(n, 44)
#a.print_list()



