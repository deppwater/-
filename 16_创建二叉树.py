class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lChild = None
        self.rChild = None


class Tree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        print(node.elem)
        print(queue[0].elem)
        while queue:
            """
            每次令queue里面存树的顶节点即queue=[1]
            然后判断顶节点的左子节点和右子节点是否有数字
            如果该节点的左子节点没有数就让该节点的左子节点等于新添加的数
            如果该节点的左子节点有数就给queue添加该节点进去即此时queue=[2] 然后判断右子节点是否有数
            如果该节点的左右都有数 此时queue=[2, 3]
            继续判断queue.pop(0)即节点2上是否有左子节点和右子节点
            如果节点2上有左子节点和右子节点 此时queue=[3, 4, 5] 则重新运行queue.pop(0)弹出3判断节点3是否有左子节点和右子节点
            """
            cur_node = queue.pop(0)
            print(cur_node.elem, 'elem')
            if cur_node.lChild is None:
                cur_node.lChild = node
                return
            else:
                queue.append(cur_node.lChild)
            if cur_node.rChild is None:
                cur_node.rChild = node
                print('---')
                return
            else:
                queue.append(cur_node.rChild)


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    print('*' * 40)
    print(tree.root.lChild.elem)