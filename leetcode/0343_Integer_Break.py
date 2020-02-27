class Solution(object):
    saved = [0] * 60
    index = -1

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= self.index:
            return self.saved[self.index]
        else:
            if self.index <= 2:
                self.saved[0] = 1
                self.saved[1] = 1
                self.saved[2] = 1
                self.index = 2
            for i in range(self.index + 1, n + 1):
                result = 1
                for j in range(1, i // 2 + 1):
                    value = max(j, self.saved[j]) * max(i - j, self.saved[i - j])
                    result = max(result, value)
                self.saved[i] = result
            self.index = max(self.index, n)
            return self.saved[n]

print(Solution().integerBreak(10))
print(Solution().integerBreak(58))