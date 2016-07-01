# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

# For example:

# Given "aacecaaa", return "aaacecaaa".

# Given "abcd", return "dcbabcd".



class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n  = len(s)
        rev = s[::-1]
        for i in range(n):
            if s[:(n - i + 1)/2] == rev[i:(n + i +1)/2]:
                return rev[:i] + s

        return rev[:-1] + s

# 按KMP算法求Prefix的方法，求Prefix, 得【0， 0， 0， 0， 0，  0， 0， 1】

class Solution(object):
    def shortestPalindrome(self, s):
        A =  s + "*" + s[::-1]
        prefix = [0]

        for i in range(1, len(A)):
            j = prefix[-1]

            while j > 0 and A[j] != A[i]:
                j = prefix[j - 1]

            prefix.append(j + (1 if A[j] == A[i] else 0))

        return s[prefix[-1]:][::-1] + s
































