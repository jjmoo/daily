class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 or not nums2:
            nums = nums1 if not nums2 else nums2
            return self.__getMid(nums)
        size = len(nums1) + len(nums2)
        return self.__getNBig(nums1, nums2, (size - 1) >> 1, size >> 1)

    def __getMid(self, nums):
        size = len(nums)
        return (nums[(size - 1) >> 1] + nums[size >> 1]) / 2

    def __getNBig(self, nums1, nums2, i, j):
        n, m = len(nums1), len(nums2)
        if n <= 2 or m <= 2:
            s, l = (nums1, nums2) if n <=2 else (nums2, nums1)
            head_l = max(0, i - 2)
            l = l[head_l:j+1]
            con = list(sorted(s + l))
            return (con[i - head_l] + con[j - head_l]) / 2
        # 0-nums, 1-size, 2-cut, 3-mid
        p1 = nums1, n, (n - 1) // 2, self.__getMid(nums1)
        p2 = nums2, m, (m - 1) // 2, self.__getMid(nums2)
        s, l = (p1, p2) if p1[3] <= p2[3] else (p2, p1)
        if i >= (m + n - 1) >> 1:
            return self.__getNBig(s[0][s[2]:], l[0], i - s[2], j - s[2])
        else:
            return self.__getNBig(s[0], l[0][:l[1]-l[2]], i, j)

    def findMedianSortedArraysLm(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 or not nums2:
            nums = nums1 if not nums2 else nums2
            return self.__getMidLm(nums, 0, len(nums) - 1)
        n1, n2 = len(nums1), len(nums2)
        return self.__getNBigLm(nums1, 0, n1 - 1, nums2, 0, n2 - 1, \
            (n1 + n2 - 1) >> 1, n1 + n2 >> 1)

    def __getMidLm(self, nums, i, j):
        return (nums[i + j >> 1] + nums[(i + j + 1) >> 1]) / 2

    def __getNBigLm(self, nums1, i1, j1, nums2, i2, j2, i, j):
        n1, n2 = j1 - i1 + 1, j2 - i2 + 1
        if n1 <= 2 or n2 <= 2:
            # 0-nums, 1-i, 2-j
            p1 = nums1, i1, j1
            p2 = nums2, i2, j2
            s, l = (p1, p2) if n1 <= 2 else (p2, p1)
            head_l = max(0, i - 2)
            con = s[0][s[1]:s[2]+1] + l[0][l[1]+head_l:l[1]+j+1]
            con = list(sorted(con))
            return (con[i - head_l] + con[j - head_l]) / 2
        # 0-nums, 1-i, 2-j, 3-size, 4-cut, 5-mid
        p1 = nums1, i1, j1, n1, (n1 - 1) // 2, self.__getMidLm(nums1, i1, j1)
        p2 = nums2, i2, j2, n2, (n2 - 1) // 2, self.__getMidLm(nums2, i2, j2)
        s, l = (p1, p2) if p1[5] <= p2[5] else (p2, p1)
        if i >= (n1 + n2 - 1) >> 1:
            return self.__getNBigLm(s[0], s[1] + s[4], \
                s[2], l[0], l[1], l[2], i - s[4], j - s[4])
        else:
            return self.__getNBigLm(s[0], s[1], s[2], \
                l[0], l[1], l[2] - l[4], i, j)


print(3.5, Solution().findMedianSortedArraysLm([3,4,5], [1,2,6]))
print(2, Solution().findMedianSortedArraysLm([1, 3], []))
print(2, Solution().findMedianSortedArraysLm([1, 3], [2]))
print(2.5, Solution().findMedianSortedArraysLm([1, 2], [3, 4]))
print(7, Solution().findMedianSortedArraysLm([1, 2, 5, 7, 9], [4, 6, 8, 9, 21, 25]))
print(8, Solution().findMedianSortedArraysLm([1, 2, 5, 7, 9], [4, 6, 8, 9, 21, 25, 50, 51]))
print(3.5, Solution().findMedianSortedArraysLm([1], [2, 3, 4, 5, 6]))
print(3.5, Solution().findMedianSortedArraysLm([1,5], [2, 3, 4, 6]))
print(4.5, Solution().findMedianSortedArraysLm([1,6], [2, 3, 4, 5, 7, 8]))
print(-1, Solution().findMedianSortedArraysLm([3], [-2,-1]))
print(2, Solution().findMedianSortedArraysLm([1,1,3,3], [1,1,3,3]))


# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
