# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

# linked list, two pointers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if head is None:
            return None

        dummy = ListNode(0)
        dummy.next = head

        fast = head
        slow = dummy

        while fast.next:
            if fast.next.val < x:
                if slow != fast:
                    next_node = fast.next.next
                    fast.next.next = slow.next
                    slow.next = fast.next
                    fast.next = next_node
                else:
                    fast = fast.next
                slow = slow.next
            else:
                fast = fast.next

        return dummy.next




class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if head is None:
            return None

        ahead, bhead = ListNode(0), ListNode(0)
        atail, btail = ahead, bhead

        while head:
            if head.val < x:
                atail.next = head
                atail = atail.next
            else:
                btail.next = head
                btail = btail.next
            head = head.next
        btail.next = None
        atail.next = bhead.next

        return ahead.next

















