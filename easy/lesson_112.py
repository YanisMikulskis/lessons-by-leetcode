
# class Base:
#     def __init__(self):
#         self.GLOBAL = 0


class TreeNode:
    def __init__(self, root=0, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

        # super().__init__()

    def make_branch(self, core):
        self.root = 5
        self.left = TreeNode(4)
        self.right = TreeNode(8)
        self.left.left = TreeNode(11)
        self.left.left.left = TreeNode(7)
        self.left.left.right = TreeNode(2)
        self.right.left = TreeNode(13)
        self.right.right = TreeNode(4)
        self.right.right.right = TreeNode(1)
        self.n = 1
    def hasPathSum(self, TreeNode, targetSum):
        self.n += 1
        targetSum -= self.root


        if targetSum == 0:
            return 1



        if self.left:
            print(self.left.hasPathSum(targetSum=targetSum))
        if self.right:
            print(self.right.hasPathSum(targetSum=targetSum))
        # targetSum -= self.root
        # if self.left is None and self.right is None and targetSum == 0:
        #     return True
        # return self.left.

    def check(self, n):




tree = TreeNode()

cores = [5,4,8,11,None,13,4,7,2,None,None,None,1]

tree.make_branch(None)
print(tree.hasPathSum(cores, 1))














