class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lChild = None
        self.rChild = None


class Tree(object):
    """二叉树"""
    def __init__(self, tree_list):
        self.root = None
        self.now_root = None
        self.now_root_index = None
        self.tree_list_length = len(tree_list)
        self.tree_list = tree_list

    def basic(self):
        item = self.tree_list[0]
        node = Node(item)
        if item is None:
            return
        else:
            self.root = node
            self.now_root = self.root
            self.now_root_index = 0
            self.makeLeftTree()
            self.makeRightTree()
            return self.root

    def makeLeftTree(self):
        if self.now_root_index * 2 + 1 > self.tree_list_length:
            return
        else:
            now_node = Node(self.tree_list[self.now_root_index * 2 + 1])
            self.now_root.lChild = now_node
            self.now_root = self.now_root.lChild
            self.now_root_index = self.now_root_index * 2 + 1

    def makeRightTree(self):
        if self.now_root_index * 2 + 2 > self.tree_list_length:
            return
        else:
            now_node = Node(self.tree_list[self.now_root_index * 2 + 2])
            self.now_root.rChild = now_node
            self.now_root = self.now_root.rChild
            self.now_root_index = self.now_root_index * 2 + 2


if __name__ == '__main__':
    tree = Tree([1, 2, 3, 4, 5, 6, 7])
    tree.basic()
    print(tree.root.elem)
    print(tree.root.lChild.elem)
    print(tree.root.lChild.rChild.elem)
