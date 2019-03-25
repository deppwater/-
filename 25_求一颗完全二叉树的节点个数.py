# 已知一棵完全二叉树，求其节点的个数
# 要求：时间复杂度低于O(N)，N为这棵树的节点个数

"""
思路：
先遍历二叉树的所有左子节点个数得到二叉树的层数h1
然后遍历二叉树头结点右子节点的所有左子节点个数得到h2
如果h1==h2 证明以头结点左子节点为root的树是满二叉树 那么左半边节点总数为2^h1-1
如果h1>h2 证明以头结点右子节点为root的树是满二叉树 那么右半边节点总数为2^h2-1
然后递归得到剩余半边子树的节点总数 最后+1
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

    def nodeNum(self, head):
        if head is None:
            return 0
        return self.bs(head, 1, self.mostLeftLevel(head, 1))

    def bs(self, node, level, h):
        if level == h:
            return 1

        if self.mostLeftLevel(node.rChild, level + 1) == h:
            # print("情况1")
            # print(h - level)
            return (1 << (h - level)) + self.bs(node.rChild, level + 1, h)
        else:
            # print("情况2")
            # print(h - level - 1)
            return (1 << (h - level - 1)) + self.bs(node.lChild, level + 1, h)

    def mostLeftLevel(self, node, level):
        while node is not None:
            level += 1
            node = node.lChild
        # print("mostLeftLevel", level - 1)
        return level - 1


if __name__ == '__main__':
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(10)
    tree.add(1)
    result = tree.nodeNum(tree.root)
    print(result)
