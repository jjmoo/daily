from typing import List
from typing import Tuple

class Solution:
    def analyse(self, seq: str) -> (int, List[tuple]):
        if not seq: return 0, []
        max_depth, valid_pairs = 0, []
        depth, start = 0, 0
        for i, ch in enumerate(seq):
            if '(' == ch:
                depth += 1
                max_depth = max(max_depth, depth)
            else:
                depth -= 1
                if 0 == depth:
                    valid_pairs.append((start, i))
                    start = i + 1
                if depth < 0:
                    return -1, []
        if 0 != depth: return -1, []
        return max_depth, valid_pairs

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        if not str: return []
        result = [0] * len(seq)
        max_depth, valid_pairs = self.analyse(seq)
        target_depth = (max_depth + 1) // 2
        for start, end in valid_pairs:
            depth = 0
            depth, i, j = 0, start, end
            while i < j and depth <= target_depth:
                if '(' == seq[i]: depth += 1
                else: depth -= 1
                i += 1
            if depth > target_depth:
                i -= 1
                while i < j and depth > 0:
                    if '(' == seq[j]: depth += 1
                    else: depth -= 1
                    j -= 1
                for k in range(i, j + 2):
                    if '(' == seq[k]:
                        if 0 == depth:
                            valid = 1
                        depth += 1
                    else:
                        if 0 == depth:
                            valid = 0
                        depth -= 1
                    result[k] = valid
        return result

    def maxDepthAfterSplit2(self, seq: str) -> List[int]:
        if not str: return []
        result = [0] * len(seq)
        depth = 0
        for i, ch in enumerate(seq):
            if '(' == ch:
                depth += 1
                result[i] = depth & 1
            else:
                result[i] = depth & 1
                depth -= 1
        return result

    def maxDepthAfterSplit3(self, seq: str) -> List[int]:
        if not str: return []
        result = [0] * len(seq)
        for i in range(1, len(seq)):
            if seq[i] == seq[i - 1]:
                result[i] = 1 - result[i - 1]
            else:
                result[i] = result[i - 1]
        return result

    def maxDepthAfterSplit4(self, seq: str) -> List[int]:
        if not str: return []
        result, flag = [], []
        cnt1, cnt2 = 0, 0
        for ch in seq:
            if '(' == ch:
                if cnt1 <= cnt2:
                    result.append(0)
                    flag.append(0)
                    cnt1 += 1
                else:
                    result.append(1)
                    flag.append(1)
                    cnt2 += 1
            else:
                f = flag.pop()
                if 0 == f:
                    result.append(0)
                    cnt1 -= 1
                else:
                    result.append(1)
                    cnt2 -= 1
        return result

    def maxDepthAfterSplit5(self, seq: str) -> List[int]:
        return [i & 1 ^ (c == '(') for i, c in enumerate(seq)]


def test(input_string):
    func = Solution().maxDepthAfterSplit5
    deep = Solution().analyse
    output_A, output_B = '', ''
    for i, v in enumerate(func(input_string)):
        if v: output_A += input_string[i]
        else: output_B += input_string[i]
    print(deep(input_string)[0], deep(output_A)[0], deep(output_B)[0])

test('(((()))((())))')
test('(()())')
test('()(())()')
test('()')


# A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" characters only, and:

# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are VPS's, or
# It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:

# depth("") = 0
# depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
# depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# For example,  "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

# Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's (and A.length + B.length = seq.length).

# Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.

# Return an answer array (of length seq.length) that encodes such a choice of A and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that even though multiple answers may exist, you may return any of them.

# Example 1:

# Input: seq = "(()())"
# Output: [0,1,1,1,1,0]
# Example 2:

# Input: seq = "()(())()"
# Output: [0,0,0,1,1,0,1,1]

# Constraints:

# 1 <= seq.size <= 10000

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
