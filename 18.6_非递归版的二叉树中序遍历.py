"""
思路：
准备一个栈 while循环条件为栈不为空或者当前节点不为空
然后开始循环 如果当前节点为空 从栈中拿一个作为当前节点并打印 当前节点向右移动 当前节点为拿出节点的右孩子
如果当前节点不为空 当前节点压入栈 然后当前节点向左移动 当前节点来到左孩子
"""


from extra.makeTree import *

import queue

tree = Tree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)


def inOrderRecur(head):
    cur_node = head.root
    help_stack = queue.LifoQueue()
    while not help_stack.empty() or cur_node is not None:
        if cur_node is not None:
            help_stack.put(cur_node)
            cur_node = cur_node.lChild
        else:
            cur_node = help_stack.get()
            print(cur_node.elem)
            cur_node = cur_node.rChild


inOrderRecur(tree)
