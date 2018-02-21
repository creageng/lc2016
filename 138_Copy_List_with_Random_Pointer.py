# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.



# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return None

        curr = head

        #cp a linked list
        while curr:
            newnode = RandomListNode(curr.label)
            newnode.next = curr.next
            curr.next = newnode
            curr = curr.next.next

        ## copy random linked pointer
        curr = head
        while curr:
            if curr.random:
                curr.next.random  = curr.random.next
            curr = curr.next.next                



        # split the constructed into two
        newhead = head.next

        pold = head
        pnew = newhead

        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next

        pold.next = None
        pnew.next = None
        return newhead









class Solution(object):
    def copyRandomList(self, head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    d = dict()
    d[None] = None
    m = head
    while head:
        if head not in d:
            cpHead = RandomListNode(head.label)
            d[head] = cpHead
            
        if head.random not in d:
            cpRandom = RandomListNode(head.random.label)
            d[head.random]=cpRandom
        
        if head.next not in d:
            cpNext = RandomListNode(head.next.label)
            d[head.next]=cpNext
            
        d[head].next = d[head.next]
        d[head].random = d[head.random]
        
        head = head.next
    return d[m]
            

























