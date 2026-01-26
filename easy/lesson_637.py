from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MakeTree:
    def __init__(self, core):
        self.tree = TreeNode(core)
        self.queue = deque([self.tree])
    def make_branch(self, values):
        current = self.queue.popleft()
        n = len(values)
        i = 1
        while i < n:
            print([i.val for i in self.queue])
            if values is not None:
                current.left = TreeNode(values[i])
                self.queue.append(current.left)
            i += 1

            if values is not None:
                current.right = TreeNode(values[i])
                self.queue.append(current.right)
            i += 1

    def in_order(self, root):
        print(f'val = {root.val if root is not None else None}')
        if root is not None:
            if root.left is not None:
                print(f'left = {root.left.val}')
            if root.right is not None:
                print(f'right = {root.right.val}')


        if root:
            self.in_order(root.left)
            self.in_order(root.right)










make = MakeTree(3)

make.make_branch([3,9,20,None,None,15,7])
make.in_order(make.tree)

class Solution:
    def averageOfLevels(self, root):
        self.root = root
        self.result = []
    def in_order(self, node):
        if node:
            if node.left and node.right:
                self.result.append((node.left + node.right)/2)
            else:
                self.result.append(node.left) if not node.right else self.root.append(node.right)
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)
#
# sol = Solution()
# sol.averageOfLevels([3,9,20,None,None,15,7])


# class Solution:
#     def __init__(self):
#         self.result = []
#
#     def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
#         if root is not None:
#             if root.left and root.right:
#                 self.result.append((root.left.val + root.right.val) / 2)
#                 print(root.left.val)
#             else:
#                 if root.left:
#                     self.result.append(root.left.val)
#                 elif root.right:
#                     self.result.apend(root.right.val)
#             print(self.result)
#             self.averageOfLevels(root.left)
#             self.averageOfLevels(root.right)
#
#     def out(self):
#         return self.result

print(f'----')
nums = [3]
num1 = 1
num2 = num1 + 1
for i in nums:
    res = i
    while num1 | num2:

    print(num1 | num2)