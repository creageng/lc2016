# Given a string S and a string T, find the minimum window in 
# S which will contain all the characters in T in complexity O(n).

# For example,
# S = "ADOBECODEBANC"
# T = "ABC"

# Minimum window is "BANC". 

# hash table, two pointer, string
# The current window is s[i:j] and the result window is s[I:J]. 
# In need[c] I store how many times I need character c (can be negative) 
# and missing tells how many characters are still missing. In the loop,
# first add the new character to the window. Then, if nothing is missing, 
# remove as much as possible from the window start and then update the result.
# https://leetcode.com/discuss/50284/12-lines-python

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = collections.Counter(t), len(t)

        i = I = J = 0

        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1

            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1

                if not J or j - i <= J - I:
                    I, J = i, j

        return s[I:J]


class Solution2(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        expected = collections.Counter(t)
        appeared = collections.Counter(t)

        count = len(t)

        start = 0
        minsize = 100000
        minstart = 0

        for end in range(len(s)):
            if s[end] in expected and expected[s[end]] > 0:
                appeared[s[end]] -= 1
                if appeared[s[end]] >= 0:
                    count -= 1

            if count == 0:

                while True:
                    if s[start] in expected and expected[s[start]] > 0:
                        if appeared[s[start]] < 0:
                            appeared[s[start]] += 1
                        else:
                            break

                    start += 1

                if minsize > end - start + 1:
                    minsize = end - start + 1
                    minstart = start


        if minsize == 100000:
            return ''
        else:
            return s[minstart:minstart+minsize]

















        # appeared = {}
        # expected = {}

        # for c in t:
        #   if c not in appeared:
        #       appeared[c] = 1
        #   else:
        #       appeared[c] += 1

        # for c in t:
        #   if c not in expected:
        #       expected[c] = 1
        #   else:
        #       expected[c] += 1

        # cnt = len(t)

        # start = 0
        # minsize =  10000
        # minstart = 0

        # for end in range(len(s)):




