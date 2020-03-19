from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return None
        from collections import Counter
        counter = Counter(nums)
        return counter.most_common(1)[0][0]

    def majorityElementVote(self, nums: List[int]) -> int:
        candidate, count = 0, 0
        for num in nums:
            if 0 == count: candidate, count = num, 1
            elif num == candidate: count += 1
            else: count -= 1
        return candidate


test = Solution().majorityElementVote
print(3, test([3,2,3]))
print(2, test([2,2,1,1,1,2,2]))


# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2
