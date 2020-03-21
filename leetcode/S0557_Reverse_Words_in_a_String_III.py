class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return s
        result, start, n = '', 0, len(s)
        for i in range(n + 1):
            if i == n or s[i] == ' ':
                for j in range(i - 1, start - 1, -1):
                    result += s[j]
                if i < n: result += ' '
                start = i + 1
        return result


test = Solution().reverseWords
print("s'teL ekat edoCteeL tsetnoc")
print(test("Let's take LeetCode contest"))


# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:

# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
