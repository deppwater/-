# 判断一个链表是否为回文结构
# 【题目】 给定一个链表的头节点head，请判断该链表是否为回
# 文结构。 例如： 1->2->1，返回true。 1->2->2->1，返回true。
# 15->6->15，返回true。 1->2->3，返回false。
# 进阶： 如果链表长度为N，时间复杂度达到O(N)，额外空间复杂
# 度达到O(1)。

"""
思路1(辅助空间为N)：
将链表压入一个栈中 然后遍历链表并与栈中每次弹出的数进行比较

思路2(辅助空间为N/2)：
准备两个指针 一个快指针一个慢指针 快指针一次走两步 慢指针一次走一步
当快指针走完的时候 慢指针刚好来到链表中间位置
然后将慢指针后面遍历的过程中压栈
然后再从头开始遍历并与栈中每次弹出的数进行比较
当栈弹完的时候还没遇到不同的数证明是回文结构

思路3(辅助空间为O(1))：
准备两个指针 一个快指针一个慢指针 快指针一次走两步 慢指针一次走一步
当快指针走完的时候 慢指针刚好来到链表中间位置
然后将慢指针右边部分的链表逆序
即当前慢指针原来指向next 现在指向None
而慢指针原来的next位置的数指向慢指针 以此类推
然后准备两个变量 一个从头开始 一个从原来的尾巴开始 每次各走一步进行比对
当有其中任何一个变量的next为None了 停止比对并将链表还原
"""
from extra.singleListNode import *

text = SingleLinkList(1)
text.add(2)
text.add(3)
text.add(3)
text.add(2)
text.add(1)


def isPalindrome(head):
    if head is None or head.next is None:
        return True

    node_slow = head
    node_fast = head

    try:
        while node_fast.next.next is not None and node_fast.next is not None:
            node_slow = node_slow.next
            node_fast = node_fast.next.next
    except Exception as e:
        pass

    node_middle = node_slow.next
    node_slow.next = None
    node_fast = None

    while node_middle is not None:
        node_fast = node_middle.next
        node_middle.next = node_slow
        node_slow = node_middle
        node_middle = node_fast

    n2 = node_slow
    n1 = head

    while n1.next is not None:
        n1 = n1.next
        n2 = n2.next
        if n1.next is None:
            print(True)
        elif n1.elem != n2.elem:
            print(False)

    n3 = node_slow
    n1 = n3.next
    n3.next = None

    # 此时n3为原来最后一个点
    # 用n1来记录n3下一个位置 即原来倒数第二个位置
    # 然后让next原先指向倒数第二个位置的n3指向本来指向的None
    # 然后进入循环：
    # 原理与之前反向后半部分基本相同
    # 先用n2记录n1的下一个位置 即原来倒数第三个位置
    # 然后将n1的next指向n3
    # n3指向现在n1的位置 n1指向现在n2的位置 然后做循环
    while n1 is not None:
        n2 = n1.next
        n1.next = n3
        n3 = n1
        n1 = n2

isPalindrome(text.head)
# print(text.head.next.next.next.elem)
text.travel()



