class Tree:
    def __init__(self,root=0,left=None, right=None):
        self.root = root
        self.left = left
        self.right = right
    def make_branch(self,val):
        if self.left is None:
            self.left = Tree(root=val)
        elif self.right is None:
            self.right = Tree(root=val)



class Solution:
    def subtreeWithAllDeepest(self, root):
        ...


sol = Solution()
sol.subtreeWithAllDeepest(root = [3,5,1,6,2,0,8,None,None,7,4])

        3
       5 1
      6 2 0 8
    n n 7 4