"""
思路：
一棵树按层遍历
如果碰到某个节点有右孩子但没有左孩子 直接返回False
如果碰到某个节点孩子不全 即除去第一种情况还有两种情况 有左没右以及左右都没有
碰到这种情况该节点之后的节点必须都是叶节点 此时需要加入一个开启判断
一旦满足开启条件 是否开启变为True 然后后续的节点必须都得是叶节点
"""

import queue


class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lChild = None
        self.rChild = None


class Tree(object):
    def __init__(self):
        self.queue = queue.Queue()
        self.root = None

    def add(self, item):
        node = Node(item)
        # if item is None:
        #     node = None
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

    def isCBT(self):
        if self.root is None:
            return True
        leaf = False
        # Node_l = None
        # Node_r = None
        self.queue.put(self.root)
        while not self.queue.empty():
            head = self.queue.get()
            Node_l = head.lChild
            Node_r = head.rChild
            if ((leaf and (Node_l is not None or Node_r is not None))
                or ((Node_l is None or Node_l.elem is None) and Node_r is not None)):
                return False
            if Node_l is not None:
                self.queue.put(Node_l)
            if Node_r is not None:
                self.queue.put(Node_r)
            else:
                leaf = True
        return True


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
    tree.add(12)
    print(tree.root.lChild.lChild.lChild.elem)
    print(tree.isCBT())
