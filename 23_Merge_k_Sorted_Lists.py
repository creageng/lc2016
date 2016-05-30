# Merge k sorted linked lists and return it as one sorted list.
#  Analyze and describe its complexity.

# Subscribe to see which companies asked this question

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    import heapq
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        # heap = []

        # for node in lists:
        #   if node:
        #       heap.append()

        heap = [(node.val, node) for node in lists if node]

        heapq.heapify(heap)

        head = ListNode(0)
        curr = head

        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val,pop[1].next))

        return head.next
        
        
