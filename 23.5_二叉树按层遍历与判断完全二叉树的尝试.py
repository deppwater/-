from extra.makeTree import *

import queue


def levelOrder(head):
    cur_node = head.root
    help_queue = queue.Queue()

    help_queue.put(cur_node)

    while not help_queue.empty():
        cur_node = help_queue.get()
        print(cur_node.elem)
        if cur_node.lChild is not None:
            help_queue.put(cur_node.lChild)
        if cur_node.rChild is not None:
            help_queue.put(cur_node.rChild)


def isCBT(head):
    """
    思路：
    一棵树按层遍历
    如果碰到某个节点有右孩子但没有左孩子 直接返回False
    如果碰到某个节点孩子不全 即除去第一种情况还有两种情况 有左没右以及左右都没有
    碰到这种情况该节点之后的节点必须都是叶节点 此时需要加入一个开启判断
    一旦满足开启条件 是否开启变为True 然后后续的节点必须都得是叶节点
    """
    cur_node = head.root
    help_queue = queue.Queue()

    help_queue.put(cur_node)
    while not help_queue.empty():
        cur_node = help_queue.get()
        if cur_node.rChild is not None and (cur_node.lChild is None or cur_node.lChild.elem is None):
            return False
        elif cur_node.rChild is not None and cur_node.lChild is not None:
            help_queue.put(cur_node.lChild)
            help_queue.put(cur_node.rChild)
        else:
            # 左边为不为空右边为空或两边都为空
            while not help_queue.empty():
                cur_node = help_queue.get()
                if cur_node.lChild is not None or cur_node.rChild is not None:
                    return False
            return True
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
    # tree.add(None)
    # tree.add(None)
    # tree.add(11)
    levelOrder(tree)
    ele = Node(11)
    tree.root.lChild.lChild.rChild = ele
    res = isCBT(tree)
    print(res)

