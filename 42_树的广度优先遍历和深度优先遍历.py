from extra.makeTree import *


test = Tree()
test.add(1)
test.add(2)
test.add(3)
test.add(4)
test.add(5)
test.add(6)
test.add(7)


def depthTree(node):
    if node is not None:
        print(node.elem)
        if node.lChild is not None:
            depthTree(node.lChild)
        # print(node.elem)
        if node.rChild is not None:
            depthTree(node.rChild)

# depthTree(test.root)


def levelQueue(node):
    if node is None:
        return
    helpLi = []
    curNode = node
    helpLi.append(curNode)
    while helpLi:
        curNode = helpLi.pop(0)
        print(curNode.elem)
        if curNode.lChild is not None:
            helpLi.append(curNode.lChild)
        if curNode.rChild is not None:
            helpLi.append(curNode.rChild)

levelQueue(test.root)
