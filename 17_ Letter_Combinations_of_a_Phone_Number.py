

# Given a digit string, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.


# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# backtracking, string


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if digits == '':
            return []

        if len(digits) == 1:
            return list(mapping[digits[0]])

        lst_letters = mapping[digits[-1]]

        prev_words = self.letterCombinations(digits[:-1])

        # res = []

        # for word in prev_words:
        #     for each in lst_letters:
        #         res.append(word+each)

        return [word+c for word in prev_words for c in lst_letters]



# class Solution:
#     # @return a list of strings, [s1, s2]
#     def letterCombinations(self, digits):
#         if '' == digits: return []
#         kvmaps = {
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz'
#         }
#         return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])




