"""
定义：
一颗树结构任何一个节点的左子树高度与右子树高度相差不超过1即为平衡二叉树

思路：
先判断一棵树的左子树是否为平衡二叉树 在判断一棵树的右子树是否为平衡二叉树
要求返回判断结果以及树的高度
"""
from extra.makeTree import *


def returnIsBT(head):
    if head is None:
        return True, 0

    left_data = returnIsBT(head.lChild)
    if left_data[0] is False:
        return False, 0

    right_data = returnIsBT(head.rChild)
    if right_data[0] is False:
        return False, 0

    if abs(left_data[1] - right_data[1]) > 1:
        return False, 0

    return True, max(left_data[1], right_data[1]) + 1


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.root.lChild.rChild = Node(4)
    tree.root.rChild.rChild = Node(5)
    tree.root.lChild.rChild.lChild = Node(6)

    res = returnIsBT(tree.root)
    print(res[0])
    print(res[1])
