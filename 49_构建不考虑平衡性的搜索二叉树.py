"""
搜索二叉树定义：
一个树的任一节点的左孩子比该节点小且右孩子比该节点大的二叉树
AVL树、红黑树、SB树等共同点是都是搜索二叉树 不同点在于对于平衡性的追求不同 没有孰好孰坏之分
"""


# 不考虑平衡性的搜索二叉树
class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lChild = None
        self.rChild = None


class SearchTree(object):
    def __init__(self):
        self.root = None

    def search(self, elem):
        if self.root is not None:
            curNode = self.root
            while curNode.elem != elem and curNode is not None:
                if curNode.elem > elem:
                    curNode = curNode.lChild
                elif curNode.elem < elem:
                    curNode = curNode.rChild
            return curNode is not None

    def add(self, elem):
        newNode = Node(elem)
        curNode = self.root
        helpNode = None
        while curNode is not None:
            helpNode = curNode
            if curNode.elem < newNode.elem:
                curNode = curNode.rChild
            elif curNode.elem > newNode.elem:
                curNode = curNode.lChild
            else:
                return 'meaningless'
        if helpNode.elem < newNode.elem:
            helpNode.rChild = newNode
        else:
            helpNode.lChild = newNode

    def delete(self, elem):
        """
        刪除的時候 假设要删除的是5 先找到5右子树上的最左节点 即比5大的数里最小的那个
        假设是6 则把6移动到5的位置 6的左孩子是原来5的左孩子 如果6有右孩子 则放在原来6的位置
        """
        curNode = self.root
        helpFather = None
        try:
            while True:
                if curNode.elem < elem:
                    helpFather = curNode
                    curNode = curNode.rChild
                elif curNode.elem > elem:
                    helpFather = curNode
                    curNode = curNode.lChild
                else:
                    break
        except (Exception,):
            pass
        if curNode.lChild is None and curNode.rChild is None:
            return self.root
        elif curNode.lChild is not None and curNode.rChild is not None:
            mostLeft = curNode.rChild
            helpNode = mostLeft
            while mostLeft is not None:
                helpNode = mostLeft
                mostLeft = mostLeft.lChild
            if helpNode != mostLeft:
                if mostLeft.rChild is None:
                    helpNode.lChild = None
                else:
                    helpNode.lChild = mostLeft.rChild
            mostLeft.lChild = curNode.lChild
            mostLeft.rChild = curNode.rChild
            if helpFather.elem > curNode.elem:
                helpFather.lChild = mostLeft
            else:
                helpFather.rChild = mostLeft
        else:
            if helpFather.elem > curNode.elem:
                helpFather.lChild = curNode.lChild if curNode.lChild is not None else curNode.rChild
            else:
                helpFather.rChild = curNode.lChild if curNode.lChild is not None else curNode.rChild


