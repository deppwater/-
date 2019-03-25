"""
三种遍历顺序的说明：
假设有一颗数的节点为1-7 即为一个三层的满二叉树
如果不考虑打印 那么递归函数来到树上节点的顺序为(当当前节点继续往下的时遇到空还会再走一遍当前节点)：
1、2、4、4(左空)、4(右空)、2、5、5、5、2、1、3、6、6、6、3、7、7、7、3、1
如果把打印时机放在第一次来到这个节点的时候为先序遍历 第二次为中序遍历 第三次为后序遍历
先序遍历：1、2、4、5、3、6、7
中序遍历：4、2、5、1、6、3、7
后序遍历：4、5、2、6、7、3、1
"""


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
        if tree is None:  # 从根节点寻找，当树不是空时
            return
        print(tree.elem)  # 打印根
        self.preOrderRecur(tree.lChild)  # 打印左子树
        self.preOrderRecur(tree.rChild)  # 打印右子树

    def inOrderRecur(self, tree):  # 中序遍历
        if tree is None:  # 从根节点寻找，当树不是空时
            return
        self.inOrderRecur(tree.lChild)  # 打印左子树
        print(tree.elem)  # 打印根
        self.inOrderRecur(tree.rChild)  # 打印右子树

    def posOrderRecur(self, tree):  # 后序遍历
        if tree is None:  # 从根节点寻找，当树不是空时
            return
        self.posOrderRecur(tree.lChild)  # 打印左子树
        self.posOrderRecur(tree.rChild)  # 打印右子树
        print(tree.elem)  # 打印根


# def preOrderRecur(nobe_head):
#     print(nobe_head.elem)
#     if nobe_head.lChild is None:
#         return
#     preOrderRecur(nobe_head.lChild)
#     if nobe_head.rChild is None:
#         return
#     preOrderRecur(nobe_head.rChild)


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