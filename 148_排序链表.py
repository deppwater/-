# Definition for singly-linked list.
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
# 示例 1:
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2:
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
import time


class ListNode:
    def __init__(self, x):
        self.elem = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.findMidNMerge(head) if head is not None else None

    def findMidNMerge(self, headNode):
        if headNode.next is None:
            return headNode
        helpNode_p = headNode
        helpNode_q = headNode
        pre = helpNode_p
        try:
            while helpNode_p.next is not None and helpNode_q.next.next is not None:
                pre = helpNode_p
                helpNode_p = helpNode_p.next
                helpNode_q = helpNode_q.next.next
        except (Exception,):
            pass
        finally:
            pre.next = None
            nodeL = self.findMidNMerge(headNode)
            nodeR = self.findMidNMerge(helpNode_p)
            return self.merge(nodeL, nodeR)

    @staticmethod
    def merge(nodeL, nodeR):
        helpNode = ListNode(0)
        curNode = helpNode
        # print(nodeL)
        # print(nodeR)
        while nodeL is not None and nodeR is not None:
            if nodeL.elem <= nodeR.elem:
                curNode.next = nodeL
                curNode = curNode.next
                nodeL = nodeL.next
            else:
                time.sleep(1)
                curNode.next = nodeR
                curNode = curNode.next
                nodeR = nodeR.next

        if nodeL is not None:
            curNode.next = nodeL

        if nodeR is not None:
            curNode.next = nodeR

        return helpNode.next


from extra.singleListNode import *

text = SingleLinkList(4)
text.append(2)
text.append(1)
text.append(3)


# print(text.head.elem)
res = Solution()
result = res.sortList(text.head)