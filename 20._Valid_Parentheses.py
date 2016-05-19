# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# Subscribe to see which companies asked this question

#stack, string


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        d = {'[':']','(':')','{':'}'}

        for e in s:
            if e in d:
                stack.append(d[e])
            elif e in d.values():
                if len(stack) == 0:
                    return False
                if e != stack.pop():
                    return False
        
        if len(stack) != 0:
            return False
        else:
            return True



