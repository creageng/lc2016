# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# For example:
# Given "25525511135",

# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter) 


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def dfs(s, level, ips, ip):
            if level == 4:
                # should be 4 parts
                if s == '':
                    ips.append(ip[1:])
                    # remove first '.'
                return

            for i in range(1, 4):
                if i <= len(s):
                    # if i > len(s), s[:i] will make false!!!!
                    if int(s[:i]) < 256:
                        dfs(s[i:], level + 1, ips, ip + '.' + s[:i])
                    if s[:i] == '0':
                        break

        ips = []
        dfs(s, 0, ips, '')
        return ips
