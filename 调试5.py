# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    count = 0
    while l1.next is not None and l2.next is not None:
        count += l1.val + l2.val
        new_node = ListNode(count)
        if not l3.root:
            l3.root = new_node
            l1 = l1.next
            l2 = l2.next
            continue
        if count >= 10:
            count = 1
        l3.next = new_node
        l3 = l3.next
        l1 = l1.next
        l2 = l2.next