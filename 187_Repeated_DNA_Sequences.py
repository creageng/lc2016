#  All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# For example,

# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # d = collections.defaultdict(str)
        
        # if len(s) < 10:
        #     return []

        d = collections.defaultdict(int)    

        for i in range(len(s) - 9):
            d[s[i : i+10]] += 1

        return [k for k, v in d.items() if v > 1]  




class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        return [k for k,v in collections.Counter([s[x:x+10] for x in range(len(s)-9)]).iteritems() if v > 1]






class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        length = len(s)
        res =[]
        if length < 10:
            return res
        dic = {}    
        for i in range(length-9):
            target = s[i:i+10]
            if target in dic:
                dic[target] += 1
            else:
                dic[target] = 1

        for k in dic:
            if dic[k] > 1:
                res.append(k) 
        
        return res
