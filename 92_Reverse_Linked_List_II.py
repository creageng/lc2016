# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,

# return 1->4->3->2->5->NULL.

# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if m < 1 or m >= n or not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # move head to m-1 th node
        for i in range(m-1):
            prev = prev.next

        # // reverse list from pre with length n-m+1 
        prev2 = None
        curr = prev.next

        for i in range(n - m + 1):
            tmp = curr.next
            curr.next = prev2
            prev2 = curr
            curr = tmp

        prev.next.next = curr
        prev.next = prev2

        return dummy.next 

        # curr = head
        # cnt = 1

        # while cnt < m:
        #     curr = curr.next
        #     cnt += 1

        # while cnt < n and curr.next:
        #     curr.next.next = curr
        #     curr = curr.next
        #     cnt += 1

        # return head



