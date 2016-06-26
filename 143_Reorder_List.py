


# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You must do this in-place without altering the nodes' values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or  not head.next:
            return 

        # find middle node
        fast = slow = head
        while True:
            if fast.next: fast = fast.next
            else: break
            if fast.next: fast, slow = fast.next, slow.next
            else: break

        # reverse the second half list
        prev, curr, head2, slow.next = slow.next, slow.next.next, slow.next, None
        while curr:
            prev.next, curr.next, head2 = curr.next, head2, curr 
            curr = prev.next

        # join the first half and the second half
        dummy2 = ListNode(0)
        dummy2.next, head2 = head2, dummy2 # add a dummy node to second half list
        prev1, curr1, prev2, curr2 = head, head.next, head2, head2.next
        while curr2:
            # insert curr2 node to first half list
            prev2.next, prev1.next, curr2.next = curr2.next, curr2, curr1 
            curr2 = prev2.next
            prev1 = curr1
            if prev1 == None: break
            curr1 = prev1.next








