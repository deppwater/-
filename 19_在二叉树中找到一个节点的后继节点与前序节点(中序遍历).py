# 在二叉树中找到一个节点的后继节点与前序节点(中序遍历)

# 该结构比普通二叉树节点结构多了一个指向父节点的parent指针。假
# 设有一 棵Node类型的节点组成的二叉树，树中每个节点的parent指针
# 都正确地指向 自己的父节点，头节点的parent指向null。只给一个在
# 二叉树中的某个节点 node，请实现返回node的后继节点的函数。在二
# 叉树的中序遍历的序列中， node的下一个节点叫作node的后继节点。

"""
找后继节点的思路：
一个节点如果有右子节点 那么他的后继节点即为他右子节点的最左子节点
是因为如果一个节点有右子树 那么当打印完该节点之后按照中序遍历一定会去找他的右子树
而他的右子树上的紧接着的第一个节点就是右子树上最左的节点
如果没有右子树 那么需要去找哪一个节点的左子节点部分最后打印的数是他
例如一个1、2、3、4、5、6、7连续构成的满二叉树
4的后继节点为2 因为首先4是2的左子节点 其次2的左子节点打印完的最后一个数也为4 因此4的后继节点为2
5的后继节点为1 是因为1的左子节点为2 2的所有子节点包括自身打印的最后一个数为5 因此5的后继节点为1

在代码中如果一个节点X没有右子节点 如果他的父节点P的左子节点是X 那么X的后继节点为P
如果P的右子节点是X 那么继续往上走 即P=P.parent X=P 继续判断
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

    @staticmethod
    def getNextNode(target_node):
        if target_node.rChild is not None:
            target_node = target_node.rChild
            while target_node.lChild is not None:
                target_node = target_node.lChild
            print('find out next node : ', target_node.elem)
        else:
            while target_node.parent is not None:
                if target_node.parent.lChild == target_node:
                    print('find out next node : ', target_node.parent.elem)
                    break
                else:
                    target_node = target_node.parent
                if target_node.parent is None:
                    print('null')
                    break

    @staticmethod
    def getLeftMost(target_node):
        if target_node.lChild is not None:
            target_node = target_node.lChild
            while target_node.rChild is not None:
                target_node = target_node.rChild
            print('find out next node : ', target_node.elem)
        else:
            while target_node.parent is not None:
                if target_node.parent.rChild == target_node:
                    print('find out next node : ', target_node.parent.elem)
                    break
                else:
                    target_node = target_node.parent
                if target_node.parent is None:
                    print('null')
                    break


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.getNextNode(tree.root.rChild.rChild)
    tree.getLeftMost(tree.root.rChild.lChild)