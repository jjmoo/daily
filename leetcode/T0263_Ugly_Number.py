class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and 2**30 * 3**19 * 5**13 % num == 0

print(Solution().isUgly(5**13))
