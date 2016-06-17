# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left justified and no extra space is inserted between words.

# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        len_words = len(words)
        i = 0
        stackLen = 0
        stack  = []
        res = []

        while i < len_words:
            curr = words[i]
            stackLen += len(curr)
            
            if stackLen <= maxWidth:
                stack.append(curr)
                stackLen += 1
            else:
                tmp = self.distribute(stack, maxWidth, False)
                res.append(tmp)

                stack = []
                stack.append(curr)
                stackLen = len(curr) + 1

            i += 1

        res.append(self.distribute(stack, maxWidth, True))

        return res

    def distribute(self, stack, maxWidth, last):
        
        res  = ''
        if last:
            if len(stack) == 1:
                res = stack[0].ljust(maxWidth)
            else:
                for wr in stack[:-1]:
                    res += wr.ljust(len(wr)+1)
                res  += stack[-1]
                res = res.ljust(maxWidth)
        else:
            if len(stack) == 1:
                res = stack[0].ljust(maxWidth)
            else:
                word_len = sum(len(wr) for wr in stack)
                space_len = maxWidth - word_len

                first = space_len%(len(stack) - 1)
                sep_len = space_len/(len(stack) - 1)

                for wr in stack[:-1]:
                    if first != 0:
                        res += wr.ljust(len(wr) + sep_len + 1)
                        first -= 1
                    else:
                        res += wr.ljust(len(wr) + sep_len)
                res += stack[-1]
        return res
        




















