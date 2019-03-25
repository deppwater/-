# 要求：
# 如果链表有环 返回第一个入环的节点 如果没环则返回none

"""
思路1：
准备一个hashSet 即没有value的hashMap
从头开始遍历链表 将遍历到的每一个值加入hashSet 在加入前判断hashSet中是否有该节点
如果判断到了相同的节点则该链表有环且该节点即为第一个入环的节点
如果遍历到了none 则该链表无环
"""

from extra.singleListNode import *


text = SingleLinkList(1)
text.append(2)
text.append(3)
text.append(4)
text.append(5)
text.append(6)

help_head = text.head
while help_head.next is not None:
    help_head = help_head.next
help_head.next = text.head.next

# text.travel()

# 使用额外空间的方法：
help_set = set()


def findLoopStart(head):
    # print('text2')
    # if head.length() < 3:
    #     return None
    cur_node = head.head
    # print(cur_node.elem)
    while cur_node is not None:
        # print('text1')
        if cur_node in help_set:
            return cur_node
        help_set.add(cur_node)
        cur_node = cur_node.next
    return None


# res = findLoopStart(text)
# print(res.elem)


"""
思路2：
准备两个指针 一个快指针一个慢指针 快指针一次走两步 慢指针一次走一步
如果快指针遇到了none 则直接返回none 如果当快指针与慢指针在一个周期中落地后位置相同 则证明有环
此时让快指针回到起点位置 且快指针变为一次走一步 快指针与慢指针再次相遇的点即为入环节点
"""

# 不使用额外空间的方法


def findLoopStart2(head):
    fast_node = head.head
    slow_node = head.head
    while fast_node.next is not None:
        if fast_node.next.next is None:
            return None
        fast_node = fast_node.next.next
        slow_node = slow_node.next
        if slow_node == fast_node:
            fast_node = head.head
            while fast_node != slow_node:
                fast_node = fast_node.next
                slow_node = slow_node.next
            return slow_node


res = findLoopStart2(text)
print(res.elem)
