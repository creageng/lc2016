# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.



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

        dummy = ListNode(0)
        dummy.next = head

        curr = head
        prev = dummy

        while prev.next:
            
            while curr.next and curr.next.val == prev.next.val:
                curr = curr.next

            if curr == prev.next:
                prev  = prev.next
                curr = curr.next
            else:
                prev.next = curr.next

        return dummy.next








        


