"""
思路：
本质上是二叉树的中序遍历 数字顺序从低到高
只不过在原本中序遍历打印的时候跟前一个元素做差值运算
并且需要额外变量记录一下上一个值
"""


import queue


class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lChild = None
        self.rChild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lChild is None:
                cur_node.lChild = node
                return
            else:
                queue.append(cur_node.lChild)
            if cur_node.rChild is None:
                cur_node.rChild = node
                return
            else:
                queue.append(cur_node.rChild)

    def inOrderRecur(self, tree):  # 中序遍历
        self.queue = queue.LifoQueue()
        self.head = tree
        self.help = list()
        while not self.queue.empty() or self.head is not None:
            if self.head is not None:
                self.queue.put(self.head)
                self.head = self.head.lChild
            else:
                self.head = self.queue.get()
                # print(self.head.elem, '+++++ elem')
                self.help.append(self.head.elem)
                # print(self.help)
                if len(self.help) > 1:
                    if self.help[-1] > self.help[-2]:
                        print(self.help[-1], '>', self.help[-2])
                        pass
                    else:
                        print('is not BinarySearchTree')
                        return
                self.head = self.head.rChild
        print('is BinarySearchTree')


if __name__ == '__main__':
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(10)
    tree.inOrderRecur(tree.root)