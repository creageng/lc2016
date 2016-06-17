# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        max_len = max(len(a), len(b))
        diff_len = abs(len(a)-len(b))

        if len(a) < len(b):
            a = '0' * diff_len + a
        else:
            b = '0' * diff_len + b

        res = ['0'] * max_len
        i = max_len - 1
        carry = 0

        while i >= 0:
            if int(a[i]) + int(b[i]) + carry == 3:
                res[i] = '1'
                carry = 1
            elif int(a[i]) + int(b[i]) + carry == 2:
                res[i] = '0'
                carry = 1
            elif int(a[i]) + int(b[i]) + carry == 1:
                res[i] = '1'
                carry = 0
            else:
                res[i] = '0'
                carry = 0

            i -= 1

        if carry == 1:
            res.insert(0, '1')

        return ''.join(res)







