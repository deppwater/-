import numpy.ma
import numpy

from numpy import *

# a1 = numpy.ma.array([1, 2, 3])
# # a2 = numpy.mat(a1)
# print(a1)
# # data5 = numpy.mat(random.randint(2, 8, size=(2, 5)))
# # print(data5)
# data1 = numpy.random.randint(2, 8, size=(2, 5))
# print(data1)
# print(data1[1])


# 进阶： 在原问题的要求之上再增加如下两个要求。
# 在左、中、右三个部分的内部也做顺序要求，要求每部分里的节点从左 到右的
# 顺序与原链表中节点的先后次序一致。 例如：链表9->0->4->5->1，pivot=3。
# 调整后的链表是0->1->9->4->5。 在满足原问题要求的同时，左部分节点从左到
# 右为0、1。在原链表中也 是先出现0，后出现1；中间部分在本例中为空，不再
# 讨论；右部分节点 从左到右为9、4、5。在原链表中也是先出现9，然后出现4，
# 最后出现5。
# 如果链表长度为N，时间复杂度请达到O(N)，额外空间复杂度请达到O(1)

# 面试中需要传递的信息：
# 1.知道什么叫稳定性
# 2.知道荷兰国旗问题不具备稳定性
# 3.直到链表问题可以省掉空间做
# 4.coding能力达标

"""
思路：
准备三个区域 small equal big 区
这里的区域只是形式上的区域 实际上操作的时候是先遍历一遍链表的节点
遍历到的第一个小于、等于、大于的节点作为每个区域的头结点
然后再次遍历整个节点 每个数判断是否小于等于大于传入的num
然后分别加在每个区域头结点的后面 最后依次合并三个区域
"""

from extra.singleListNode import *

text = SingleLinkList(1)
text.append(3)
text.append(5)
text.append(7)
text.append(8)
text.append(6)
text.append(4)
text.append(2)
text.append(4)
text.append(2)
text.append(0)


def listPartition(head, num):
    sH = None  # small head
    sT = None  # small tail
    eH = None  # equal head
    eT = None  # equal tail
    bH = None  # big head
    bT = None  # big tail
    # pre_node = head
    # while pre_node is not None:
    #     if pre_node.elem < num:
    #         sH = pre_node
    #         sT = sH
    #         break
    #     pre_node = pre_node.next
    #
    # pre_node = head
    # while pre_node is not None:
    #     if pre_node.elem == num:
    #         eH = pre_node
    #         eT = eH
    #         # print(eT.next.elem)
    #         break
    #     pre_node = pre_node.next
    #
    # pre_node = head
    # while pre_node is not None:
    #     if pre_node.elem > num:
    #         bH = pre_node
    #         bT = bH
    #         break
    #     pre_node = pre_node.next

    # print(sT.elem)
    # print(eT.elem)
    # print(bT.elem)
    # print('=' * 20)
    # # print(bH.next.next.next.elem)
    # print(head.elem)

    while head is not None:
        if head.elem < num:
            help_node = head
            head = head.next
            sH = help_node
            print(sH.elem)
            # print(sH.next.elem)
            # print(sH.next.next.elem)
            sH = sH.next
            # print('-' * 30)
        elif head.elem == num:
            help_node = head
            # print(help_node.elem)
            head = head.next
            eH = help_node
            eH = eH.next
        elif head.elem > num:
            help_node = head
            head = head.next
            bH = help_node
            bH = bH.next
    # sT.next = None
    # eT.next = None
    # bT.next = None
    # print(sH.elem)
    # print(sH.next.elem)

    # print(eT.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.elem)
    # print(sH.next.next.next.elem)
    #
    if eH and bH:
        eH.next = bH
    if sH:
        sH.next = eH if eH else bH

    if sH:
        return sH
    elif not sH and eH:
        return eH
    else:
        return bH


def travel(head):
    if head:
        cur_node = head
        while cur_node:
            print(cur_node.elem)
            cur_node = cur_node.next


def length(head):
    if head:
        cur = 1
    else:
        return 0
    cur_node = head
    while cur_node.next is not None:
        cur_node = cur_node.next
        cur += 1
    return cur


res = listPartition(text.head, 5)
travel(res)
# print(res.next.elem)
# length(res)
