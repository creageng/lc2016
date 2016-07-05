# https://discuss.leetcode.com/topic/14987/108-ms-17-lines-body-explained

# The idea is to do line sweep and just process the buildings only at the start 
# and end points. The key is to use a priority queue to save all the buildings 
# that are still "alive". The queue is sorted by its height and end time (the 
#     larger height first and if equal height, the one with a bigger end time first). 

# For each iteration, we first find the current process time, which is either 
# the next new building start time or the end time of the top entry of the live queue. 
# If the new building start time is larger than the top one end time, then process the one
#  in the queue first (pop them until it is empty or find the first one that ends after the 
#     new building); otherswise, if the new building starts before the top one ends,
#      then process the new building (just put them in the queue). After processing, 
# output it to the resulting vector if the height changes.
#  Complexity is the worst case O(NlogN)

from heapq import *

class Solution(object):
    def getSkyline(self, buildings):
        # buildings, buildings
        skyline = []
        i, n = 0, len(buildings)
        liveHR = []

        while i < n or liveHR:

            if not liveHR or i < n and buildings[i][0] <= - liveHR[0][1]:
                # L
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    # (height, right) pairs are kept in the priority queue
                    # H, R
                    # The queue is sorted by its height and end time
                    heappush(liveHR, (-buildings[i][2], -buildings[i][1]))
                    i += 1

            else:
                x = -liveHR[0][1]
                # pop them until it is empty or 
                # find the first one that ends after the new building)
                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)
            
            height = len(liveHR) and -liveHR[0][0]

            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
                 # skyline += [x, height], 
                 # wrong

        return skyline


# class Solution(object):
#     def getSkyline(self, buildings):
#         """
#         :type buildings: List[List[int]]
#         :rtype: List[List[int]]
#         """

#         events = sorted([(L, -H, R) for L, R, H in buildings]) \
#         			+ list(set(R, 0, None) for L, R, H in buildings)


#         res = [[0, 0]]
#         # X, height
#         hp = [(0, float("int"))]

#         for x, negH, R in events:

#         	while x >= hp[0][1]:
#         		heappop(hp)

#         	if negH:
#         		heappush(hp, (negH, R))

#         	if res[-1][1] + hp[0][0]:
#         		res.append([x, -hp[0][0]])

#         return res[1:]

