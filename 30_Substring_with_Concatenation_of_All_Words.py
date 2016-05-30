#  You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]

# You should return the indices: [0,9].
# (order does not matter). 



class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        res = []
        
        if len(s) == 0 or len(words) == 0:
            return []

        wordsTotal = len(words) * len(words[0])

        for i in range(len(s)-wordsTotal+1):
            currWords = [s[j: j+len(words[0])] for j in range(i, i+wordsTotal,len(words[0]))]

            for word in words:
                if word in currWords:
                    currWords.remove(word)
                else:
                    break
            if not currWords:
                res.append(i)

        return res                  


