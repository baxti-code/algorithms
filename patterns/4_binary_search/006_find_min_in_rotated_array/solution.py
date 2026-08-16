"""
# leetcode 153. Find Minimum in Rotated Sorted Array
Difficulty: Medium

Time Complexity: O(log n)
Space Complexity: O(1)

"""

class Solution:
    def findMin(nums):
        l, r = 0, len(nums) -1

        while l < r:
            m = (l+r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m

        return nums[l]

            