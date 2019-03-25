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
            self.root.parent = None
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lChild is None:
                cur_node.lChild = node
                cur_node.lChild.parent = cur_node
                return
            else:
                queue.append(cur_node.lChild)
            if cur_node.rChild is None:
                cur_node.rChild = node
                cur_node.rChild.parent = cur_node
                return
            else:
                queue.append(cur_node.rChild)


"""
思路：
一个节点如果有右子节点 那么他的后继节点即为他右子节点的最左子节点
是因为如果一个节点有右子树 那么当打印完该节点之后按照中序遍历一定会去找他的右子树
而他的右子树上的紧接着的第一个节点就是右子树上最左的节点
如果没有右子树 那么需要去找哪一个节点的左子节点部分最后打印的数是他
例如一个1、2、3、4、5、6、7连续构成的满二叉树
4的后继节点为2 因为首先4是2的左子节点 其次2的左子节点打印完的最后一个数也为4 因此4的后继节点为2
5的后继节点为1 是因为1的左子节点为2 2的所有子节点包括自身打印的最后一个数为5 因此5的后继节点为1

在代码中如果一个节点X没有右子节点 如果他的父节点P的左子节点是X 那么X的后继节点为P
如果P的右子节点是X 那么继续往上走 即X=P P=P.parent 继续判断
"""


def getSuccessorNode(node):
    if node is None:
        return node

    if node.rChild is not None:
        cur_node = node.rChild
        while cur_node.lChild is not None:
            cur_node = cur_node.lChild
        return cur_node

    else:
        cur_node = node
        cur_par = node.parent
        while cur_par is not None:
            if cur_par.lChild == cur_node:
                return cur_par
            cur_node = cur_par
            cur_par = cur_par.parent
        return None


"""
思路：
与找后继节点的逻辑对称 
如果一个节点有左子树 那么去找左子树上最右的节点
如果一个节点没有左子树 那么找他的父节点 如果他的父节点的右子节点是他 那么结果就是他的父节点
如果不是则继续向上查找
"""


def getLeftMost(node):
    if node is None:
        return None

    if node.lChild is not None:
        cur_node = node.lChild
        while cur_node.rChild is not None:
            cur_node = cur_node.rChild
        return cur_node

    else:
        cur_node = node
        cur_par = node.parent
        while cur_par is not None:
            if cur_par.rChile ==  cur_node:
                return cur_par
            cur_node = cur_par
            cur_par = cur_par.parent
        return None


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    res1 = getSuccessorNode(tree.root.rChild.rChild)
    res2 = getSuccessorNode(tree.root.lChild.lChild)
    res3 = getSuccessorNode(tree.root.rChild.lChild)
    print(res1)
    print(res2.elem)
    print(res3.elem)


