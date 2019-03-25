"""
遍历规则：
来到的当前节点记为cur：
1.如果cur没有左孩子 cur向右移动 即cur=cur.rChild 即原来的cur的右孩子上
2.如果cur有左孩子 找到cur左子树上最右的节点 记为mostRight：
  1.1.如果mostRight的rChild指针指向none 让其指向cur cur向左移动 即cur=cur.lChild
  1.2.如果mostRight的rChild指针指向cur 让其指向none cur向右移动 即cur=cur.rChild


以一个节点值为1-7的完全二叉树为例：
首先cur指向头结点head 根据规则 cur有左孩子 那么先找到cur左子树的最右节点即节点5
此时5指向none 那么让5的rChild指针指向cur 然后cur=cur.lChild 来到节点2
与上述过程相同 那么4的rChild指向cur cur=cur.lChild 来到节点4
此时cur没有左孩子 那么cur=cur.rChild cur又回到了2
此时cur有左孩子 且cur的mostRight节点的rChild指向cur即指向2 那么让mostRight即4的rChild指针指向none
此时cur=cur.rChild来到了5
......

注意：
1.让4指向2的时候不需要建立额外的节点 只需要添加一个是否指向cur的判断
2.那么整个便利过程cur来到的顺序为 1、2、4、2、5、1、3、6、3、7
3.如果某节点有左孩子 cur指针会回到该节点两次 否则只来到一次 也可以认为没有左子树的情况下第一次和第二次是和在一起的
4.如果该节点左子树最右节点指向none 那么一定是第一次来到该节点 如果指向cur 那么一定是第二次
5.递归版的遍历只要节点不为none 那么一定能来到该节点3次 而通过在第1、2、3次来到该节点的时候加入打印操作可以构成先序中序和后序遍历
6.morris遍历cur只来到一个节点两次 在第一次来到该节点的时候打印为先序遍历 在第二次来到该节点的时候打印为中序遍历
而不考虑只来到过一次的节点 只考虑来到过两次的那些借点 例子中的情况就是1、2、3 在第二次来到这些节点的时候逆序打印该节点左子树的右边界
并且在最后再逆序打印一次整个树的右边界
"""

from extra.makeTree import *

tree = Tree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)


# morris先序遍历
def morris(head):
    curNode = head
    while curNode is not None:
        if curNode.lChild is None:
            print(curNode.elem)
            curNode = curNode.rChild
        else:
            mostRight = curNode.lChild
            while mostRight.rChild is not None and mostRight.rChild != curNode:
                mostRight = mostRight.rChild
            if mostRight.rChild is None:
                print(curNode.elem)
                mostRight.rChild = curNode
                curNode = curNode.lChild
            else:
                mostRight.rChild = None
                curNode = curNode.rChild


morris(tree.root)
print('-' * 30)


# morris中序遍历
def morris(head):
    curNode = head
    while curNode is not None:
        if curNode.lChild is None:
            print(curNode.elem)
            curNode = curNode.rChild
        else:
            mostRight = curNode.lChild
            while mostRight.rChild is not None and mostRight.rChild != curNode:
                mostRight = mostRight.rChild
            if mostRight.rChild is None:
                mostRight.rChild = curNode
                curNode = curNode.lChild
            else:
                print(curNode.elem)
                mostRight.rChild = None
                curNode = curNode.rChild


morris(tree.root)
print('-' * 30)


# morris后序遍历
def morris(head):
    curNode = head
    while curNode is not None:
        if curNode.lChild is None:
            curNode = curNode.rChild
        else:
            mostRight = curNode.lChild
            while mostRight.rChild is not None and mostRight.rChild != curNode:
                mostRight = mostRight.rChild
            if mostRight.rChild is None:
                mostRight.rChild = curNode
                curNode = curNode.lChild
            else:
                mostRight.rChild = None
                printEdge(curNode.lChild)
                curNode = curNode.rChild
    printEdge(head)


def printEdge(node):
    preNode = node
    if preNode is not None:
        curNode = preNode.rChild
    else:
        return
    preNode.rChild = None
    # 将原先顺序的rChild指向逆序后打印
    while curNode is not None:
        helpNode = curNode
        curNode = curNode.rChild
        helpNode.rChild = preNode
        # 这里扣的时候要注意此时的helpNode才是原先的curNode 此时的curNode已经到了下一个位置
        preNode = helpNode
    # print(preNode)
    if preNode is not None:
        # print(preNode.rChild)
        while preNode is not None:
            print(preNode.elem)
            preNode = preNode.rChild
    # 再将逆序后的指针还原 该过程与上述类似就不写了


morris(tree.root)