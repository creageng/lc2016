# Write a program to find the node at which the intersection of two singly linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        tmpA = headA
        tmpB = headB
        na = 0
        nb = 0

        # get the length of two lists
        while tmpA:
            tmpA = tmpA.next
            na += 1

        while tmpB:
            tmpB = tmpB.next
            nb += 1

        tmpA = headA
        tmpB = headB

        while na > 0 and nb >0:
            if na == nb:
                if tmpA == tmpB:
                    return tmpA
                else:
                    tmpA = tmpA.next
                    tmpB = tmpB.next

                    na -= 1
                    nb -= 1

            elif na > nb:
                na -= 1
                tmpA = tmpA.next

            else:
                nb -= 1
                tmpB = tmpB.next

        return None



















