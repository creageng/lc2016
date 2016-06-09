# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# tag: hash table, array


# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """

#         d = {}
#         for word in strs:
#           sortedWord = ''.join(sorted(word))
#           d[sorted] = [word] if sortedWord not in d else d[sortedWord] + [word]


#           res = []
#           for kw in d:
#               if len(d[kw]) >= 2:
#                   res += d[kw]

#           return res
        


# class Solution(object):
#     def groupAnagrams(self, strs):
#        d = collections.defaultdict(list)
#        for s in strs:
#            d[tuple(sorted(s))].append(s)  
#        return [a for agram_group in d.values() if len(agram_group)>1 for a in agram_group]


from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):

        d = defaultdict(list)
        for w in strs:
            d[''.join(sorted(w))] += [w]

        return d.values()






















