# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Subscribe to see which companies asked this question


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k == 0:
            return head

        if head == None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        curr  = dummy

        length = 0
        while curr.next:
            length += 1
            curr = curr.next

        curr.next = dummy.next
        #connect tail to head

        steps = length - (k%length)

        for i in range(steps):
            curr  = curr.next

        head = curr.next
        curr.next = None

        return head







