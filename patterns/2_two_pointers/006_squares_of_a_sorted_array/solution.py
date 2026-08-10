"""
#977 leetcode - "Squares of a sorted array"
Difficulty : Easy

Time complexity : O(n)
Space complexity : O(n)

"""

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l, r = 0, n-1
        res = [0] * n
        pos = n -1
    
        while l <= r:
            l_sq = nums[l] ** 2 
            r_sq = nums[r] ** 2
            if r_sq > l_sq:
                res[pos] = r_sq
                r -= 1
            else:
                res[pos] = l_sq
                l += 1
            pos -= 1
        return res
