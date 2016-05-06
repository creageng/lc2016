class Solution:
    # @return an integer
    def myAtoi(self, s):
        INT_MAX = 2147483647; INT_MIN = -2147483648

        i = 0
        sum = 0
        sign = 1

        while i < len(s) and s[i].isspace():
            i += 1

        if i < len(s) and s[i] == "-":
            sign = -1

        if i < len(s) and (s[i] == "-" or s[i] == "+"):
            i += 1

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            if INT_MAX/10 >= sum:
                sum *= 10
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN

            if INT_MAX - digit >= sum:
                sum += digit
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            i += 1

        return sign * sum