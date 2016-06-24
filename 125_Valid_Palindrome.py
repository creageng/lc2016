# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.



class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        newS = []

        for e in s:
            if '0' <= e <= '9' or \
                'a' <= e <= 'z':
                newS.append(e)
            elif 'A' <= e <= 'Z':
                newS.append(chr(ord(e) - ord('A') + ord('a')))

        if newS == newS[::-1]:
            return True
        else:
            return False
            