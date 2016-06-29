# Sort a linked list using insertion sort.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# for i ← 1 to length(A)-1
#     j ← i
#     while j > 0 and A[j-1] > A[j]
#         swap A[j] and A[j-1]
#         j ← j - 1
#     end while
# end for

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # large pointer
        curr = head
        while curr.next:
            if curr.next.val < curr.val:
                prev = dummy
                # scan from begining untll bigger or equal
                while prev.next.val < curr.next.val:
                    prev = prev.next

                tmp = curr.next
                curr.next = tmp.next

                tmp.next = prev.next
                prev.next = tmp

            else:
                curr = curr.next

        return dummy.next



class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        dummy = ListNode(0)

        while head:
            walker = dummy
            curr = head.next

            while walker.next and walker.next.val < head.val:
                walker = walker.next

            head.next = walker.next
            walker.next = head
            head = curr

        return dummy.next

# Two key points are: (1) a quick check see if the new value is
 # already the largest 
 # 2) only refresh the search pointer p 
# when the target is before it, in other words smaller.

class Solution:
    def insertionSortList(self, head):
        p = dummy = ListNode(0)
        cur = dummy.next = head

        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue

            if p.next.val > val:
                p = dummy

            while p.next.val < val:
                p = p.next

            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new

        return dummy.next







































