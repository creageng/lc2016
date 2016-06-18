# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        # dummy = ListNode(0)
        # dummy.next = head

        # prev = dummy
        # curr = head
        curr = head

        while curr:

            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
                 # skip duplicated node


            curr = curr.next
            # not duplicate of current node, move to next node

        return head


    
