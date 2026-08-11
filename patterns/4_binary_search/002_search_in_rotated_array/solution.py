"""
# leetcode 33. Search in Rotated Sorted Array
Difficulty: Medium

This problem is a classic example of binary search. The key idea is to first find the index of the minimum element in the rotated sorted array, which will help us determine the two sorted subarrays. Once we have the index of the minimum element, we can perform a standard binary search on the appropriate subarray based on the target value.

Time Complexity: O(log n) 
Space Complexity: O(1)

"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
 
        while l < r:
            m = (l + r) // 2
 
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
 
        min_i = l
 
        if min_i == 0:
            l, r = 0, n - 1
        elif target >= nums[0] and target <= nums[min_i - 1]:
            l, r = 0, min_i - 1
        else:
            l, r = min_i, n - 1
 
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1