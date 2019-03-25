class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lChild = None
        self.rChild = None


class Tree(object):
    """
    二叉树:
    先构建该节点的左子节点 再构建该节点的右子节点 然后以当前节点下一个位置的节点作为父节点重复构建
    建一个辅助队列来存放节点信息
    每次开始构建左子节点的时候pop(0)作为父节点 并添加新的左子节点到辅助队列
    构建右子节点的时候则不进行pop操作 直接添加新的右子节点到辅助队列
    若当前节点index值为i 那么他的左子节点的index为2*i+1 右子节点index为2*i+2 父节点index为(i-1)/2
    """
    def __init__(self, tree_list):
        self.help_li = list()
        self.now_index = 0
        self.boolean = True
        self.now_node = None
        # 不需要修改的值
        self.root = None
        self.tree_list_length = len(tree_list)
        self.tree_list = tree_list

    def basic(self):
        item = self.tree_list[0]
        node = Node(item)
        if item is None:
            return
        else:
            self.root = node
            # self.root.parent = None
            # self.now_node = self.root
            # self.now_index += 1
            self.help_li.append(self.root)
            while self.now_index + 1 < self.tree_list_length:
                if self.boolean:
                    self.makeLeftTree()
                else:
                    self.makeRightTree()
            return self.root

    def makeLeftTree(self):
        if self.now_index + 1 < self.tree_list_length:
            # 构建一个节点 该节点为当前节点的左子节点
            lChild_node = Node(self.tree_list[self.now_index + 1])
            # 每次开始构建节点的时候需要从节点列表中取第一个作为父节点
            self.now_node = self.help_li.pop(0)
            # 将构建的节点作为当前节点的左子节点
            self.now_node.lChild = lChild_node
            # 添加节点到列表
            self.help_li.append(self.now_node.lChild)
            # now_index是被构建的节点的坐标
            self.now_index += 1
            self.boolean = not self.boolean
        else:
            return

    def makeRightTree(self):
        if self.now_index + 1 < self.tree_list_length:
            rChild_node = Node(self.tree_list[self.now_index + 1])
            self.now_node.rChild = rChild_node
            # 添加节点到列表
            self.help_li.append(self.now_node.rChild)
            self.now_index += 1
            self.boolean = not self.boolean
        else:
            return


if __name__ == '__main__':
    tree = Tree([1, 2, 3, 4, 5, 6, 7])
    tree.basic()
    print(tree.root.elem)
    print(tree.root.lChild.elem)
    print(tree.root.rChild.elem)
    print(tree.root.lChild.lChild.elem)
    print(tree.root.rChild.rChild.elem)
