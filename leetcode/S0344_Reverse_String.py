from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s: return
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

#  

# Example 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
