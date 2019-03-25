"""
思路：
本质上是二叉树的中序遍历 数字顺序从低到高
只不过在原本中序遍历打印的时候跟前一个元素做差值运算
并且需要额外变量记录一下上一个值
"""

from extra.makeTree import *

import queue


def inOrderRecur(head):
    cur_node = head.root
    help_queue = queue.LifoQueue()
    pre_node = None
    while not help_queue.empty() or cur_node is not None:
        if cur_node is not None:
            # pre_node = cur_node
            help_queue.put(cur_node)
            cur_node = cur_node.lChild
        else:
            cur_node = help_queue.get()
            # print(pre_node.elem)
            if pre_node is not None:
                if pre_node.elem >= cur_node.elem:
                    return False
            # print(cur_node.elem)
            pre_node = cur_node
            # print('-' * 30)
            cur_node = cur_node.rChild
    return True


tree = Tree()
tree.add(5)
tree.add(3)
tree.add(8)
tree.add(2)
tree.add(4)
tree.add(6)
tree.add(10)

res = inOrderRecur(tree)
print(res)
