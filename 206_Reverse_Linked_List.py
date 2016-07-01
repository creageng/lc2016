# # Reverse a singly linked list.

# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head
            
        prev = head
        curr = head.next
        prev.next = None

        while curr:
            tmp = curr.next
            curr.next = prev

            prev = curr
            curr = tmp

        return prev








# Recursion

class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)




    