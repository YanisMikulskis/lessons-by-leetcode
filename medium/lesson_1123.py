#
#
class Tree:
    def __init__(self, core):
        self.core = core
        self.left = None
        self.right = None
    def make_branch(self, new_core):
        if new_core < self.core:
            if self.left is None:
                self.left = Tree(new_core)
            else:
                self.left.make_branch(new_core)
        else:
            if self.right is None:
                self.right = Tree(new_core)
            else:
                self.right.make_branch(new_core)
    def inorder(self, node):
        if node:
            print(f'val = {node.core}')
            self.inorder(node.left)

            self.inorder(node.right)
    def level_order(self, tree):
        if not tree:
            return

        queue = [tree]
        while queue:
            current = queue.pop(0)
            print(current.core, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
class NodeTree:
    def __init__(self, core, cores):
        self.core = core
        self.left, self.right = None, None
        self.cores = cores

    def level_build(self, node):
        if self.cores:
            if node:
                node.left = NodeTree(self.cores.pop(0), self.cores)
                node.right = NodeTree(self.cores.pop(0), self.cores)
                self.level_build(node.left)
                self.level_build(node.right)

    def level_order(self, tree):
        if not tree:
            return
        queue, nodes, kori = [tree], [], None
        while queue:
            exp_queue = [i.core for i in queue]
            if len(exp_queue) == 2:
                nodes = exp_queue
            if None not in exp_queue and len(exp_queue) == 3:
                kori = exp_queue[0]
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        else:
            result = [el for el in [kori] + nodes if el]
            return result

















#
#
# tree = Tree(10)
# tree.make_branch(7)
# tree.make_branch(12)
#
#
# tree.make_branch(6)
# tree.make_branch(9)
#
# tree.make_branch(11)
# tree.make_branch(13)

#
# tree.level_order(tree)
# root = [3,5,1,6,2,0,8,None,None,7,4]
# node = NodeTree(3, [5,1,6,2,0,8,None,None,7,4])
# node.level_build(node)
# print(node.level_order(node))


node = NodeTree(0, [1,3,None,2])

node.level_build(node)
print(node.level_order(node))
#
# class MyClass:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#         self.c = 3  # "Защищенный" атрибут
#         self.d = 4  # "Приватный" атрибут
#
# obj = MyClass()
# print(vars(obj))
# node = NodeTree(0, [1,3,None,2])
# node.level_build(node)
# node.level_order(node)

# for i in root[1:]:
#     node.level_build(i)


a = 10
arr = [a]
a_new = arr.pop(0)




# def thesaurus_adv(*users):
#     users = list(map(lambda x: x.split(), list(users)))
#     key_lastnames = {
#         lastname[1][0]: {
#             name[0][0]:[] for name in users if name[0][1] == lastname[0][1]
#         } for lastname in users
#     }
#
#     for user in users:
#         key_lastnames[user[1][0]][user[0][0]].append(' '.join(user))
#     print(key_lastnames)
#     #
#     # for last in users:
#     #     key_lastnames[]
#
# thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева')