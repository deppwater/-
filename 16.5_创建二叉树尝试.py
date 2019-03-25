class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lChild = None
        self.rChild = None


class Tree(object):
    def __init__(self, root):
        self.root = Node(root)
        self.help_li = list()
        self.help_li.append(self.root)

    def add(self, num):
        node = Node(num)
        # 设置一个当前节点列表 在构建右子节点的时候弹出0位置的节点 其余情况只要添加节点就将节点添加至列表
        # self.help_li.append(self.root)
        # print(self.help_li)
        while self.help_li:
            cur_node = self.help_li[0]
            if cur_node.lChild is None:
                cur_node.lChild = node
                self.help_li.append(node)
                return
            # self.help_li.append(cur_node.lChild)
            if cur_node.rChild is None:
                cur_node.rChild = node
                self.help_li.append(node)
                self.help_li.pop(0)
                return
            # self.help_li.append(cur_node.rChild)


text = Tree(1)
text.add(2)
text.add(3)
text.add(4)
text.add(5)
text.add(6)
text.add(7)
print(text.root.rChild.rChild.elem)