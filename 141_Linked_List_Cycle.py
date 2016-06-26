#  Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space? 




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False

        fast = head
        slow = head
        iscycle = False

        while fast.next:
            fast = fast.next.next
            if fast is None:
                break
            
            slow = slow.next
            if fast == slow:
                iscycle = True
                break

        return iscycle