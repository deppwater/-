"""
思路：
准备一个栈 先将头结点放入
从栈中弹出一个节点作为当前的头结点 打印改值
如果当前节点右孩子不为空 压入右孩子
如果当前节点左孩子不为空 压入左孩子
继续上述循环 需要注意的是到达最后一层时及时当前节点没有左孩子也没有右孩子也要从栈中弹出

extra：
压入和弹出栈的过程相当于访问了一个节点两次 但做不到像递归函数一样访问三次
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


def preOrderRecur(head):
    if head.root is not None:
        root = head.root
        q = queue.LifoQueue()
        q.put(root)
        while not q.empty():
            # 弹出的节点恰好就为当前需求的头结点
            # 且过程中来不及出现栈为空的情况
            cur_head = q.get()
            print(cur_head.elem)
            if cur_head.rChild is not None:
                q.put(cur_head.rChild)
            if cur_head.lChild is not None:
                q.put(cur_head.lChild)


preOrderRecur(tree)
