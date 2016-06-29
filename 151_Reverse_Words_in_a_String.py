#  Given an input string, reverse the string word by word.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the". 


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        return " ".join(l[::-1]).strip()


