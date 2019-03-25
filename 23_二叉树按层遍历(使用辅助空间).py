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

    def levelOrder(self):
        if self.root is None:
            return
        q = list()
        q.append(self.root)
        while q:
            current = q.pop(0)
            print(current.elem, end='   ')
            if current.lChild is not None:
                q.append(current.lChild)
            if current.rChild is not None:
                q.append(current.rChild)


if __name__ == '__main__':
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(10)
    tree.add(None)
    tree.add(None)
    tree.levelOrder()
