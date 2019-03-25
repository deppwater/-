"""
思路1：
使用hashSet 遍历第一个链表然后加入hashSet
然后遍历第二个链表判断并返回第一次在hashSet里找到的节点
如果遍历到none都没有找到证明两个链表不相交

思路2：
不使用额外空间 需要注意的是如果两个链表相交了 那么从相交的点开始以后的点完全一样
首先拿到两个链表的长度length1和length2 以及末尾节点end1和end2
然后比较end1和end2的地址 如果相等证明相交 反之直接返回False
接着比较length1和length2的大小 假设length1比length2大20
那么链表1头结点先走20步 然后链表1与链表2同步走 直到第一次指向同样的地址即为第一个交点

注意：
如果一个链表有环一个链表无环 由于是单链表结构 所以不可能相交
"""

from extra.singleListNode import *

nodeList1 = SingleLinkList(1)
nodeList1.append(2)
nodeList1.append(3)
nodeList1.append(4)
nodeList1.append(5)
nodeList1.append(6)

nodeList2 = SingleLinkList(7)
nodeList2.append(8)
# 设置两个链表的第一个交点为4
nodeList2.head.next.next = nodeList1.head.next.next


# 不使用额外空间
def findCrossLink(head1, head2):
    length1 = head1.length()
    length2 = head2.length()
    endNode1 = head1.head
    endNode2 = head2.head

    while endNode1.next is not None:
        endNode1 = endNode1.next

    while endNode2.next is not None:
        endNode2 = endNode2.next

    if endNode1 != endNode2:
        return False

    endNode1 = head1.head
    endNode2 = head2.head
    # 当不太好想需要走几步的时候可以假设length1==length2 那么两者差值为0 且需要走0步 以此类推
    if length1 > length2:
        for _ in range(length1 - length2):
            endNode1 = endNode1.next
    elif length1 < length2:
        for _ in range(length2 - length1):
            endNode2 = endNode2.next

    while endNode1 != endNode2:
        endNode1 = endNode1.next
        endNode2 = endNode2.next

    return endNode1


res = findCrossLink(nodeList1, nodeList2)
print(res.elem)
