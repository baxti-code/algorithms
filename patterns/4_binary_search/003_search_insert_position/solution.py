"""
# leetcode 35 - Search index position
Difficulty : Easy

Time complexity : O(log n)
Space complexity : O(1)

"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1

        while l<=r:
            m = (l+r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m -1

        return l
            
            