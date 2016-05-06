
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = ''
        maxL = 0

        l = 0
        r = 0

        while l < len(s)-1:
            sub  = s[l]
            r = l + 1
            
            while r < len(s):
                if s[r] in sub:
                    if len(sub) > maxL:
                        maxL = len(sub)
                        res = sub+s[r]
                else:
                    sub += s[r]
                r += 1

            l += 1

        return res  

# time limit exceeded

        # for i in range(len(s)-1):
        #   for j in range(i+1, len(s)):
        #       currSub = s[i:j-1]
        #       if s[j] in currSub:
        #           if len(currSub) > maxL:
        #               maxL = len(currSub)
        #               res = currSub
                
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        maxL = 0
        l = 0
        r = 0
        sub = ''

        while r < len(s):

            if s[r] not in sub:
                r += 1
            else:
                while s[l] != s[r]:
                    l += 1
                l += 1

            sub = s[l:r]
            maxL = max(maxL, len(sub))
        
        return maxL





