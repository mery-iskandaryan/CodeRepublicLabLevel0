class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Hashtable:
    def __init__(self, size):
        self.size = size
        self.array = [None for _ in range(self.size)]

    def my_hash(self, key):
        return hash(key) % self.size

    def insert(self, dict_key, value):
        node = Node(dict_key, value)
        index = self.my_hash(dict_key)

        if self.array[index] is None:
            self.array[index] = node
            return

        current = self.array[index]
        while current.next:
            if current.key == dict_key:
                current = node
                return
            current = current.next
        current.next = node

    def get(self, key):
        index = self.my_hash(key)
        current = self.array[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError("Key is not present...")

    def remove(self, key):
        index = self.my_hash(key)
        current = self.array[index]
        if current.key == key:
            self.array[index] = current.next
            return

        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
        raise KeyError("Key is not present...")

    def get_keys(self):
        keys = []
        for el in self.array:
            if el:
                while el:
                    keys.append(el.key)
                    el = el.next
        return keys

    def get_values(self):
        values = []
        for el in self.array:
            if el:
                while el:
                    values.append(el.value)
                    el = el.next
        return values

    def get_items(self):
        items = []
        for el in self.array:
            if el:
                while el:
                    items.append((el.key, el.value))
                    el = el.next
        return items

    def clear(self):
        self.size = 0
        self.array = []

    def display(self):
        for el in self.array:
            if el:
                print((el.key, el.value))
                while el.next:
                    el = el.next
                    print((el.key, el.value))


h = Hashtable(5)
h.insert('a', 1)
h.insert('b', 2)
h.insert('c', 3)
h.insert('d', 4)
h.insert('e', 5)
h.display()
# print(h.get('a'))
# h.remove('e')
# h.remove('a')
# print()
# h.display()
# print(h.get_keys())
# print(h.get_values())
# print(h.get_items())
h.clear()
h.display()
