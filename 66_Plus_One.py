# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.


#array, mathc


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        carry  = 1

        for i in range(len(digits)-1, -1, -1):
            curr = digits[i]
            curr += carry

            if curr >= 10:
                digits[i] = curr - 10
                carry = 1
            else:
                carry = 0
                digits[i] = curr
                break

        if i == 0 and carry == 1:
            digits.insert(0, 1)

        return digits
