# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# Subscribe to see which companies asked this question

# dynamic programming; string

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxLen = 0
        last = -1

        for i in range(len(s)):
            if s[i] == ')':
                if not stack:
                    last  = i
                else:
                    stack.pop()
                    if not stack:
                        maxLen = max(maxLen, i-last)
                    else:
                        maxLen = max(maxLen, i-stack[-1])
            else:
                stack.append(i)

        return maxLen

