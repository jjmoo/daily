from typing import List
from utils import Benchmark

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0: return -1
        memo, min_coins = {0:0}, min(coins)
        def dp(i = amount):
            if i not in memo:
                if i < min_coins: return 999999999
                elif i in coins: memo[i] = 1
                else: memo[i] = 1 + min((dp(i - x) for x in coins))
            return memo[i]
        cnt = dp()
        return cnt if cnt < 999999999 else -1

    def coinChangeBetter(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0: return -1
        memo, min_coins, coins = {0:0}, min(coins), list(sorted(coins, reverse=True))
        def dp(i = amount):
            if i not in memo:
                if i < min_coins: return 999999999
                elif i in coins: memo[i] = 1
                else: memo[i] = 1 + min((dp(i - x) for x in coins))
            return memo[i]
        cnt = dp()
        return cnt if cnt < 999999999 else -1

    def coinChangeGreedy(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0: return -1
        n, coins, MAX = len(coins), list(sorted(coins, reverse=True)), 999999999
        def greedy(ans = MAX, count = 0, index = 0, money=amount):
            if 0 == money: return count
            if index >= n: return MAX
            x = money // coins[index]
            while x >= 0 and x + count < ans:
                ans = min(ans, greedy(ans, x + count, index + 1, money - x * coins[index]))
                x -= 1
            return ans
        cnt = greedy()
        return cnt if cnt < MAX else -1


def test(method, name):
    with Benchmark(name):
        print(3, method([1, 2, 5], 11))
        print(-1, method([2], 3))
        print(3, method([1, 2, 5], 5465))

# test(Solution().coinChange, 'coinChange')
# test(Solution().coinChange, 'coinChangeBetter')
test(Solution().coinChangeGreedy, 'coinChangeGreedy')


# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/coin-change
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
