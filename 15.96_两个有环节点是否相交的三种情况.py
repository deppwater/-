"""
首先获取两个链表的头结点head1和head2 以及两个链表第一次进入自身循环的节点loop1和loop2
然后分为以下三种情况（当loop1与loop2都为空时两个链表都无环 参考上一个案例 当其中一个为空时不可能相交）

情况1：
两个链表不相交
判断条件为loop1不等于loop2 只有这个条件的时候也可能是情况3
所以此时要额外判断一下 如果loop1接着往下走能碰到loop2 就是情况3 如果碰到自己了 就是情况1
此时直接返回false

情况2：
两个链表先相交再进入同一个环
判断条件为loop1==loop2
此时如果去掉环的部分即相当于两个无环单链表相交的情况(要注意入环节点的位置)
即可以得到第一次相交的点

情况3：
两个链表从同一个环的不同位置进入环
判断条件在情况1当中
那么此时第一个相交的节点可以是loop1也可以是loop2
返回其中任意一个即可
"""

from extra.singleListNode import *

# 两个不相交的环
situation11 = SingleLinkList(1)
situation11.append(2)
situation11.append(3)
situation11.append(4)
situation11.append(5)
situation11.append(6)
situation11.head.next.next.next.next.next.next = situation11.head.next.next.next

situation12 = SingleLinkList(1.1)
situation12.append(2.2)
situation12.append(3.3)
situation12.append(4.4)
situation12.append(5.5)
situation12.append(6.6)
situation12.head.next.next.next.next.next.next = situation12.head.next.next.next


# 情况2当中的环 第一次相交节点为3 第一次入环节点为4
situation21 = SingleLinkList(1)
situation21.append(2)
situation21.append(3)
situation21.append(4)
situation21.append(5)
situation21.append(6)
situation21.head.next.next.next.next.next.next = situation21.head.next.next.next

situation22 = SingleLinkList(1.1)
situation22.head.next = situation21.head.next.next


# 情况3中的环 入环节点节点1为4 节点2为6
situation31 = SingleLinkList(1)
situation31.append(2)
situation31.append(3)
situation31.append(4)
situation31.append(5)
situation31.append(6)
situation31.head.next.next.next.next.next.next = situation31.head.next.next.next

situation32 = SingleLinkList(1.1)
situation32.append(2.2)
situation32.head.next.next = situation31.head.next.next.next.next.next


def getSituation(node1, node2):
    res1 = node1.findLoopStart()
    res2 = node2.findLoopStart()
    # print(res1.elem)
    # print(res2.elem)
    if res1 == res2:
        return findLoop2(node1, res1, node2, res2)
    else:
        help_res1 = res1
        help_res1 = help_res1.next
        while help_res1 != res1:
            help_res1 = help_res1.next
            if help_res1 == res2:
                return res1, res2
        return None


def findLoop2(node1, loop1, node2, loop2):
    end1 = node1.head
    end2 = node2.head
    head1 = node1.head
    head2 = node2.head
    # 两个链表长度的差值
    n = 0

    while end1 != loop1:
        end1 = end1.next
        n += 1
    while end2 != loop2:
        end2 = end2.next
        n -= 1
    # print(n)

    if n > 0:
        while n != 0:
            head1 = head1.next
            n -= 1
    elif n < 0:
        while n != 0:
            head2 = head2.next
            n += 1
    # print(head1.elem)
    # print(head2.elem)
    # print(head1.next)
    # print(head2.next)

    while head1 != head2:
        head1 = head1.next
        head2 = head2.next
    # print(head1)
    # print(head2)
    return head2


result1 = getSituation(situation11, situation12)
print(result1)
print('-' * 50)

result2 = getSituation(situation21, situation22)
print(result2.elem)
print('-' * 50)

result3 = getSituation(situation31, situation32)
print(result3[0].elem)
print(result3[1].elem)
print('-' * 50)
