# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

# Here is an example of version numbers ordering:

# 0.1 < 1.1 < 1.2 < 13.37


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        # lv1 = [int(e) for e in version1.split('.')]
        # lv2 = [int(e) for e in version2.split('.')]
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        while len(v1) and int(v1[-1]) == 0:
            v1 = v1[:-1]
        v1 = [int(e) for e in v1]
        
        while  len(v2) and int(v2[-1]) == 0:
            v2 = v2[:-1]
        
        v2 = [int(e) for e in v2]

        n1 = len(v1)
        n2 = len(v2)
        minn = min(n1, n2)
        print v1,v2, minn

        p = 0
        while p < minn:
            if v1[p] < v2[p]:
                return -1
            elif v1[p] > v2[p]:
                return 1
            else:
                p += 1

        if n1 == minn < n2:
            return -1

        elif n1 > minn == n2:
            return 1
        else:
            return 0