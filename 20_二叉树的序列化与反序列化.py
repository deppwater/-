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

    def stringSerialByPre(self, head):
        if head is None:
            return '#!'
        string_res = str(head.elem) + '!'
        string_res += self.stringSerialByPre(head.lChild)
        string_res += self.stringSerialByPre(head.rChild)
        return string_res

    def reconByPreString(self, result):
        result_list = result.split('!')
        result_list.pop()
        print(result_list)
        # self.help = queue.Queue()
        # for i in result_list:
        #     self.help.put(i)
        return self.reconPreOrder(result_list)

    def reconPreOrder(self, result_list):
        if len(result_list) == 0:
            return None
        value = result_list.pop(0)
        if value != '#':
            root = Node(int(value))
            root.lChild = self.reconPreOrder(result_list)
            root.rChild = self.reconPreOrder(result_list)
            return root


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    res = tree.stringSerialByPre(tree.root)
    print(res)
    print(type(res))
    last = tree.reconByPreString(res)
    print(last.rChild.rChild.elem)