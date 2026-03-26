class TreeNode:
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right


    def make_branch(self, el):
        if self.left is None:
            self.left = TreeNode(el)
        elif self.right is None:
            self.right = TreeNode(el)
        else:
            if self.left.left is None or self.left.right is None:
                self.left.make_branch(el)
