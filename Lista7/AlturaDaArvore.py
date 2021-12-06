class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def inOrderNonRecursive(self, vals):
        stack = []
        current = self
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                vals.append(current.val)
                current = current.right
        return vals

    def traverseByLevel(self, vals):
        queue = [self]
        while queue:
            node = queue.pop(0)
            vals.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

    def height(self):
        if self.size() <= 1:
            return 0
        else:
            return self.heightTwo()

    def heightTwo(self):
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return 1 + self.right.heightTwo()
        if self.right is None:
            return 1 + self.left.heightTwo()
        return 1 + max(self.left.heightTwo(), self.right.heightTwo())

    def size(self):
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return 1 + self.right.size()
        if self.right is None:
            return 1 + self.left.size()
        return 1 + self.left.size() + self.right.size()


root = BSTNode()
lista = list(map(int, input().split()))
for v in lista:
    root.insert(v)

print(root.height())
