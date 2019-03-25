"""
思路：
准备两个栈 因为先序遍历的顺序为中左右 而具体实现的时候为先压右孩子再压左孩子
那么将顺序变为先压左孩子再压右孩子 顺序就会变成中右左 反过来就是后序遍历的顺序左右中
那么可以用第二个栈储存本来需要打印的数 最后再依次弹出并打印
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


# 还有一种只是用一个栈的方法
def posOrderRecur(head):
    help_stack1 = queue.LifoQueue()
    help_stack_out = queue.LifoQueue()
    head_node = head.root

    help_stack1.put(head_node)

    while not help_stack1.empty():
        cur_node = help_stack1.get()
        help_stack_out.put(cur_node)
        if cur_node.lChild is not None:
            help_stack1.put(cur_node.lChild)
        if cur_node.rChild is not None:
            help_stack1.put(cur_node.rChild)

    while not help_stack_out.empty():
        print(help_stack_out.get().elem)


posOrderRecur(tree)
