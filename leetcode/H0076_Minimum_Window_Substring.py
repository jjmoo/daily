class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ''
        from collections import Counter
        target, counter = Counter(t), Counter()
        count, start, n = len(target), 0, len(s)
        min_len, min_start, min_end, found = n, 0, n, False
        for i, ch in enumerate(s):
            if ch in target:
                counter[ch] += 1
                if not found and counter[ch] == target[ch]:
                    count -= 1
                    found = 0 == count
                if found:
                    while True:
                        while s[start] not in target:
                            start += 1
                        if counter[s[start]] > target[s[start]]:
                            counter[s[start]] -= 1
                            start += 1
                        else:
                            cur_len = i - start + 1
                            if cur_len < min_len:
                                min_len, min_start, min_end = cur_len, start, i
                            break
        return '' if not found else s[min_start : min_end + 1] 


test = Solution().minWindow
print('BANC', test('ADOBECODEBANC', 'ABC'))


# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-window-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
