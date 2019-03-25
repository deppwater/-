# 复制含有随机指针节点的链表
# 【题目】 一种特殊的链表节点类描述如下：
# public class Node { public int value; public Node next; public
# Node rand;
# public Node(int data) { this.value = data; }
# }
# Node类中的value是节点值，next指针和正常单链表中next指针的意义
# 一样，都指向下一个节点，rand指针是Node类中新增的指针，这个指
# 针可能指向链表中的任意一个节点，也可能指向null。 给定一个由
# Node节点类型组成的无环单链表的头节点head，请实现一个函数完成
# 这个链表中所有结构的复制，并返回复制的新链表的头节点。 进阶：
# 不使用额外的数据结构，只用有限几个变量，且在时间复杂度为 O(N)
# 内完成原问题要实现的函数。


"""
思路：
准备一个hashMap 里面存放的键为每个节点 值为每个节点的赋值 但next指针和rand指针都指向空
如 1对应1' 2对应2' 以此类推
然后因为1的next是可以找到2的 因此根据查表可以找到2'
那么1'的next指针就是1'找到的2的键对应的值即2'
通过同样的的方式可以找到1'的rand指向 重复上述操作
"""

import queue

from extra.singleListNode import *


class NodeWithRand(SingleLinkList):
    def __init__(self, elem):
        super().__init__(elem)
        self.elem = elem
        head_node = Node(elem)
        self.head = head_node
        self.next = None
        self.rand = None


# class NodeWithRand(object):
#     def __init__(self, elem):
#         self.elem = elem
#         self.next = None
#         self.rand = None


text = NodeWithRand(1)
text2 = text.append(2)
text3 = text.append(3)
text4 = text.append(4)
text5 = text.append(5)
text6 = text.append(6)
# print(text.head.next.elem)
# 1->6 2->6 3->5 4->3 5->none 6->4
text.head.rand = text.head.next.next.next.next.next
text.head.next.rand = text.head.next.next.next.next.next
text.head.next.next.rand = text.head.next.next.next.next
text.head.next.next.next.rand = text.head.next.next
text.head.next.next.next.next.rand = None
text.head.next.next.next.next.next.rand = text.head.next.next.next

rand = NodeWithRand(1.1)
rand.append(2.2)
rand.append(3.3)
rand.append(4.4)
rand.append(5.5)
rand.append(6.6)
# print(rand.head.next)
# rand2 = NodeWithRand(2)
# rand3 = NodeWithRand(3)
# rand4 = NodeWithRand(4)
# rand5 = NodeWithRand(5)
# rand6 = NodeWithRand(6)
# print(text3.elem)


# 使用额外辅助hashMap完成
def copyListWithRand(head):
    help_dict = dict()
    help_queue_cus = queue.Queue()
    help_queue_new = queue.Queue()
    # help_dict[text1.head] = rand1
    # help_dict[text2] = rand2
    # help_dict[text3] = rand3
    # help_dict[text4] = rand4
    # help_dict[text5] = rand5
    # help_dict[text6] = rand6
    old_head = head.head
    new_head = rand.head
    while old_head is not None:
        help_dict[old_head] = new_head
        help_queue_cus.put(old_head)
        help_queue_new.put(new_head)
        old_head = old_head.next
        new_head = new_head.next

    for _ in range(head.length()):
        old_node = help_queue_cus.get()
        new_node = help_queue_new.get()
        # print(old_node.rand)
        if old_node.next is None:
            new_node.next = None
        else:
            new_node.next = help_dict[old_node.next]
        if old_node.rand is None:
            new_node.rand = None
            # new_node.elem = None
        else:
            new_node.rand = help_dict[old_node.rand]

    # print(rand.head.rand.elem)
    return rand

# res = copyListWithRand(text)
# print(res.head.rand.elem)
# print(res.head.next.rand.elem)
# print(res.head.next.next.rand.elem)
# print(res.head.next.next.next.rand.elem)
# print(res.head.next.next.next.next.rand)
# print(res.head.next.next.next.next.next.rand.elem)




# 不用hashMap解决问题
"""
思路：
让原来的1节点的next指向1' 1'的next指向2 2指向2' 以此类推
然后让1'的rand指针指向1的rand对应的rand' 此时1的rand'即为1的rand的next
链接完毕所有的节点之后分离新旧链表
"""


def copyListWithRand2(head):
    new_node = rand.head
    old_node = head.head
    # while new_node.next is not None:
    # print(text.head.next.next.next.rand.elem)
    for _ in range(head.length()):
        # old_node.next = new_node
        # new_node.next = help_old_node.next
        # old_node = help_old_node.next
        # new_node = help_new_node.next

        next_cur_node = old_node.next
        # print(next_cur_node.elem)
        # print('=' * 30)
        next_new_node = new_node.next
        # print(next_new_node.elem)
        # print('=' * 30)
        old_node.next = new_node
        old_node.next.next = next_cur_node
        # print(old_node.next.elem)
        old_node = next_cur_node
        new_node = next_new_node
        # old_node.next = next_new_node

    # print(text.head.next.next.next.next.next.elem)

    old_node = head.head
    new_node = head.head.next
    # print(old_node.rand)
    # print(old_node.rand.elem)
    # print(new_node.next.elem)
    try:
        for _ in range(head.length() // 2):
            # print('text')
            # print(old_node.rand.elem)
            if old_node.rand is None:
                # print('text')
                new_node.rand = None
            else:
                new_node.rand = old_node.rand.next
            new_node = new_node.next.next
            old_node = old_node.next.next
    except Exception as e:
        pass

    head.head = head.head.next
    cur_node = head.head
    for _ in range(head.length() // 2):
        cur_node.next = cur_node.next.next
        cur_node = cur_node.next
    return head

res = copyListWithRand2(text)
# 1->6 2->6 3->5 4->3 5->none 6->4
print(res.travel())
print('+' * 40)
print(res.head.rand.elem)
print(res.head.next.rand.elem)
print(res.head.next.next.rand.elem)
print(res.head.next.next.next.rand.elem)
print(res.head.next.next.next.next.rand)
print(res.head.next.next.next.next.next.rand.elem)
# print(res.head.next.next.next.next.next.rand.elem)
# print(res.head.next.next.next.next.next.next.next.rand.elem)
# print(res.head.next.next.next.next.next.next.next.next.next.rand)
# print(res.head.next.next.next.next.next.next.next.next.next.next.next.rand.elem)

