"""
链表的题主要考察的coding能力是尽量缩小辅助空间
"""


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self, elem):
        head_node = Node(elem)
        self.head = head_node

    def isEmpty(self):
        return self.head is None

    def length(self):
        if self.head:
            cur = 1
        else:
            return 0
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            cur += 1
        return cur

    def travel(self):
        if self.head:
            cur_node = self.head
            while cur_node is not None:
                print(cur_node.elem)
                cur_node = cur_node.next

    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = node
        return node

    def add(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            node, self.head = self.head, node

    def insert(self, pos, item):
        node = Node(item)
        result = self.length()
        if pos > result or pos < 0:
            ex = Exception('pos参数错误')
            raise ex
        cur_node = self.head
        cur_set = 1
        while pos > cur_set:
            cur_node = cur_node.next
            cur_set += 1
        if pos == 0:
            node.next = cur_node
        else:
            node.next = cur_node.next
            cur_node.next = node

    def search(self, item):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.elem == item:
                return True
            cur_node = cur_node.next
        return False

    def delete(self, item):
        cur_node = self.head
        pre_node = None
        if not self.search(item):
            ex = Exception('参数错误')
            raise ex
        if cur_node.elem == item:
            self.head = cur_node.next
            return
        while cur_node.elem != item:
            pre_node = cur_node
            cur_node = cur_node.next
        pre_node.next = cur_node.next

    def findLoopStart(self):
        fast_node = self.head
        slow_node = self.head
        while fast_node.next is not None:
            if fast_node.next.next is None:
                return None
            fast_node = fast_node.next.next
            slow_node = slow_node.next
            if slow_node == fast_node:
                fast_node = self.head
                while fast_node != slow_node:
                    fast_node = fast_node.next
                    slow_node = slow_node.next
                return slow_node


if __name__ == '__main__':
    text = SingleLinkList(1)
    text.append(2)
    text.append(3)
    text.append(4)
    text.append(5)
    text.travel()
    res = text.length()
    print(res)
    text.insert(1, 6)
    print('=' * 30)
    text.travel()
    print('=' * 30)
    text.insert(6, 7)
    text.travel()
    print('=' * 30)
    res = text.search(7)
    print(res)
    print('=' * 30)
    text.delete(2)
    print(text.head.elem)
    text.travel()



