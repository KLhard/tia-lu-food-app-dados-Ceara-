class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Rotação
        x.right = y
        y.left = T2

        # Atualiza alturas
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Rotação
        y.left = x
        x.right = T2

        # Atualiza alturas
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, node, key, value=None):
        # Inserção normal em BST
        if not node:
            return Node(key, value)
        elif key < node.key:
            node.left = self.insert(node.left, key, value)
        else:
            node.right = self.insert(node.right, key, value)

        # Atualiza altura
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        # Verifica balanceamento
        balance = self.get_balance(node)

        # Left Left
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Left Right
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Right
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Right Left
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def inorder(self, node, lista):
        if not node:
            return
        self.inorder(node.left, lista)
        lista.append(node.value)
        self.inorder(node.right, lista)
