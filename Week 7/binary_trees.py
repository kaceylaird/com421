class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def setChild(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)

            else:
                self.left.setChild(value)

        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.setChild(value)


class BinaryTree:
    def __init__(self):
        self.root = None

    def insertNode(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.setChild(value)

    def printFrom(self, node):
        if node is not None:
            self.printFrom(node.left)
            print(node.value)
            self.printFrom(node.right)
