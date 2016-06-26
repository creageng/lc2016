# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Note: Do not modify the linked list.

# Follow up:
# Can you solve it without using extra space?

# X和K的关系是基于Y互补的。等于说，两个指针相遇以后，
# 再往下走X步就回到Cycle的起点了。这就可以有O(n)的实现了。



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head:
        #     return False

        fast = head
        slow = head
        iscycle = False

        while fast and fast.next:
            fast = fast.next.next            
            slow = slow.next

            if fast == slow:
                fast = head
                while fast is not slow:
                    fast = fast.next
                    slow = slow.next
                return fast

        return None

