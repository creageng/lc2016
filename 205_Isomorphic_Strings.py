
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        if not s and not t:
            return True

        if not s or not t:
            return False


        sd = collections.defaultdict(str)
        td = collections.defaultdict(str)

        for i in range(len(s)):
            if s[i] in sd or t[i] in td:
                if sd[s[i]] != t[i] or td[t[i]] != s[i]:
                    return False
            else:
                sd[s[i]] = t[i]
                td[t[i]] = s[i]

        return True






class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        mapping = {}
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] == t[i]:
                    continue
                else:
                    return False
            else:
                if t[i] in mapping.values():
                    return False
                else:
                    mapping[s[i]] = t[i]

        return True






def isIsomorphic3(self, s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))



def isIsomorphic5(self, s, t):
    return map(s.find, s) == map(t.find, t)









    
