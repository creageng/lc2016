# Implement wildcard pattern matching with support for '?' and '*'.
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false


# dynamic programming, backtracking, greedy, string

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sp = 0
        pp = 0
        pStar = -1
        sStar = 0

        while sp < len(s):
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == "?"):
                pp += 1
                sp += 1
                continue

            if pp < len(p) and p[pp] == "*":
                sStar = sp
                pStar = pp
                pp += 1
                continue

# If not match, then we check if there is a * previously showed up,
# if there is no *,  return false;
# if there is an *,  we set current p to the next element of *, 
#  and set current s to the next saved s position.

            if pStar != -1:
                pp = pStar + 1
                sStar += 1
                sp = sStar
                continue
            else:
                return False


        while pp < len(p) and p[pp] == "*":
            pp += 1

        if pp == len(p):
            return True
        else:
            return False
