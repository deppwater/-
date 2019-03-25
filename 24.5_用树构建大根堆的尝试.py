import queue


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.lChild = None
        self.rChild = None
        self.parent = None


class MakeHeap(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        help_queue = [self.root]
        while help_queue:
            cur_node = help_queue.pop(0)
            if cur_node.lChild is None:
                cur_node.lChild = node
                cur_node.lChild.parent = cur_node
                cur_node = cur_node.lChild
                while cur_node.parent is not None and cur_node.parent.elem < cur_node.elem:
                    par_node = cur_node.parent
                    par_node.elem, cur_node.elem = cur_node.elem, par_node.elem
                    cur_node = par_node
                return
            else:
                help_queue.append(cur_node.lChild)
            if cur_node.rChild is None:
                cur_node.rChild = node
                cur_node.rChild.parent = cur_node
                cur_node = cur_node.rChild
                while cur_node.parent is not None and cur_node.parent.elem < cur_node.elem:
                    par_node = cur_node.parent
                    par_node.elem, cur_node.elem = cur_node.elem, par_node.elem
                    cur_node = par_node
                return
            else:
                help_queue.append(cur_node.rChild)

    def levelOrder(self):
        cur_node = self.root
        help_queue = queue.Queue()

        help_queue.put(cur_node)

        while not help_queue.empty():
            cur_node = help_queue.get()
            print(cur_node.elem)
            if cur_node.lChild is not None:
                help_queue.put(cur_node.lChild)
            if cur_node.rChild is not None:
                help_queue.put(cur_node.rChild)

if __name__ == '__main__':
    tree = MakeHeap()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(10)
    tree.levelOrder()

    # print(tree.root.lChild.lChild.parent.elem)
