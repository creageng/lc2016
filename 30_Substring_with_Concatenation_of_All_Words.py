#  You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]

# You should return the indices: [0,9].
# (order does not matter). 



class Solution1(object):
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




class Solution2(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        from collections import defaultdict

        c = Counter(words)
        m = len(words)
        n = len(words[0])
        res = []
        total_length = m * n

        for k in range(n):
            left = k
            subd = defaultdict(int)
            count = 0
            #loop over the string
            for j in range(k, len(s)-n+1, n):
                #get a word from observed substring
                word = s[j:j+n]
                #check if it is a valid word
                if word in c:
                    subd[word] += 1
                    count += 1
                ##Shift the window as long as we have encountered more 
                # number of a word than is needed
                    while subd[word] > c[word]:
                        subd[s[left:left+n]] -= 1
                        left += n
                        count -= 1
                    if count  == m:
                        res.append(left)
                        
                else:
                    left = j + n
                    subd = defaultdict(int)
                    count = 0
        
        return res


        




