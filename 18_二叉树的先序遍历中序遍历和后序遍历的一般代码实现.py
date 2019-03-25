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

    def preOrderRecur(self, tree):  # 前序遍历
        self.queue = queue.LifoQueue()
        self.head = tree
        if self.head is not None:
            self.queue.put(self.head)
        while True:
            self.head = self.queue.get()
            print(self.head.elem)
            if self.head.rChild is not None:
                self.queue.put(self.head.rChild)
            if self.head.lChild is not None:
                self.queue.put(self.head.lChild)
            if self.queue.empty():
                break

    def inOrderRecur(self, tree):  # 中序遍历
        self.queue = queue.LifoQueue()
        self.head = tree
        while not self.queue.empty() or self.head is not None:
            if self.head is not None:
                self.queue.put(self.head)
                self.head = self.head.lChild
            else:
                self.head = self.queue.get()
                print(self.head.elem)
                self.head = self.head.rChild

    def posOrderRecur(self, tree):  # 后序遍历
        self.queue = queue.LifoQueue()
        self.help = queue.LifoQueue()
        self.head = tree
        if self.head is not None:
            self.queue.put(self.head)
        while True:
            self.head = self.queue.get()
            self.help.put(self.head)
            if self.head.rChild is not None:
                self.queue.put(self.head.lChild)
            if self.head.lChild is not None:
                self.queue.put(self.head.rChild)
            if self.queue.empty():
                break
        while not self.help.empty():
            print(self.help.get().elem)


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.preOrderRecur(tree.root)
    print('=' * 30)
    tree.inOrderRecur(tree.root)
    print('=' * 30)
    tree.posOrderRecur(tree.root)