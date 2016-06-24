# Determine whether an integer is a palindrome. 
# Do this without extra space.

# click to show spoilers.

# Subscribe to see which companies asked this question


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        if x == 0:
            return True

        div = 1

        while x/div >= 10:
            div *= 10

        while x:
            left = x/div
            right = x%10

            if right != left:
                return False

            x = (x%div)/10
            div /= 100

        return True

        











if __name__ == "__main__":
    x = 22422
    print Solution().isPalindrome(x)
    #"PAHNAPLSIIGYIR"
    ## [1,2]