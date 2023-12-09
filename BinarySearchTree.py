class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        return self.root is None

    def insert(self, key, value):
        self.size += 1
        self.root = self._help_insert(self.root, key, value)

    def _help_insert(self, node, key, value):
        if node is None:
            return Node(key, value)
        elif node.key > key:
            node.left = self._help_insert(node.left, key, value)

        elif node.key < key:
            node.right = self._help_insert(node.right, key, value)

        else:
            node.value = value
        return node

    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def find_max(self, node):
        current = node
        while current.right:
            current = current.right
        return current

    def contains(self, key):
        current = self.root
        while current:
            if current.key == key:
                return True
            if current.key < key:
                current = current.right
            else:
                current = current.left
        return False

    def search(self, key):
        current = self.root
        while current:
            if current.key == key:
                return current.value
            if current.key < key:
                current = current.right
            else:
                current = current.left
        return "There is no node with this key..."

    def clear(self):
        self.root = None

    def update(self, key, value):
        current = self.root
        while current:
            if current.key == key:
                current.value = value
                break
            if current.key < key:
                current = current.right
            else:
                current = current.left

    def inorder(self):
        res = []
        self._help_inorder(self.root, res)
        return res

    def _help_inorder(self, node, result):
        if node:
            self._help_inorder(node.left, result)
            result.append((node.key, node.value))
            self._help_inorder(node.right, result)

    def preorder(self):
        res = []
        self._help_preorder(self.root, res)
        return res

    def _help_preorder(self, node, result):
        if node:
            result.append((node.key, node.value))
            self._help_preorder(node.left, result)
            self._help_preorder(node.right, result)

    def postorder(self):
        res = []
        self._help_postorder(self.root, res)
        return res

    def _help_postorder(self, node, result):
        if node:
            self._help_postorder(node.left, result)
            self._help_postorder(node.right, result)
            result.append((node.key, node.value))

    def height(self):
        res = self._help_height(self.root)
        return res

    def _help_height(self, node):
        if not node:
            return -1
        else:
            left = self._help_height(node.left)
            right = self._help_height(node.right)
        return max(left, right) + 1

    def delete(self, key):
        self.root = self._help_delete(self.root, key)
        return self.root

    def _help_delete(self, node, key):
        if not node:
            return None
        elif key < node.key:
            node.left = self._help_delete(node.left, key)
        elif key > node.key:
            node.right = self._help_delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                tmp = self.find_min(node.right)
                node.key, node.value = tmp.key, tmp.value
                node.right = self._help_delete(node.right, tmp.key)
        return node

    def kth_smallest(self, k):
        ls = self.inorder()
        return ls[k-1]

    def kth_largest(self, k):
        return self.inorder()[-k]

    def copy(self):
        new_tree = BinaryTree()
        new_tree.root = self._help_copy(self.root)
        return new_tree

    def _help_copy(self, node):
        if not node:
            return node
        new_tree = Node(node.key, node.value)
        new_tree.left = self._help_copy(node.left)
        new_tree.right = self._help_copy(node.right)
        return new_tree


b = BinaryTree()
b.insert(10, 'a')
b.insert(8, 'e')
b.insert(15, 'b')
b.insert(7, 'c')
b.insert(12, 'd')
b.insert(20, 'f')
b.insert(1, 'g')
b.insert(-10, 'h')
b.insert(5, 'm')
# print(b.search(5))
# b.update(5, 'updated')
# print(b.find_min(b.root))
# print(b.find_max(b.root))
# # print(b.search(16))
# print(b.search(5))
# # print(b.size)
# print(b.inorder())

# # print(b.postorder())
# print(b.height())
# print(b.inorder())
# b.delete(6)
# b.delete(18)
print(b.inorder())
# print(b.kth_smallest(3))
# print(b.kth_largest(2))
a = b.copy()
print(a.inorder())
