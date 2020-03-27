from typing import List

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]: return 0
        from collections import deque
        result, n = 0, len(M)
        for i in range(n):
            if M[i][i]:
                result += 1
                queue = deque()
                queue.append(i)
                while queue:
                    j = queue.popleft()
                    M[j][j] = 0
                    for k in range(n):
                        if M[j][k] and M[k][k]:
                            queue.append(k)
        return result

    def findCircleNumDisjoint(self, M: List[List[int]]) -> int:
        if not M or not M[0]: return 0
        from collections import Counter
        n = len(M)
        disjoint = [-1] * n
        def find(x):
            if -1 == disjoint[x]:
                return x
            disjoint[x] = find(disjoint[x])
            return disjoint[x]
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if ry != rx:
                disjoint[ry] = rx
        for i in range(n - 1):
            for j in range(i + 1, n):
                if M[i][j]:
                    union(i, j)
        return Counter(disjoint)[-1]


test = Solution().findCircleNum
print(2, test([[1,1,0], [1,1,0], [0,0,1]]))
print(1, test([[1,1,0], [1,1,1], [0,1,1]]))
print(1, test([[1,0,1], [0,1,1], [1,1,1]]))
print(1, test([[1,1,1], [1,1,1], [1,1,1]]))


# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

# Example 1:

# Input: 
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
# The 2nd student himself is in a friend circle. So return 2.
# Example 2:

# Input: 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
# Note:

# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/friend-circles
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
