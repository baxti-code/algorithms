"""
# leetcode 42. Trapping Rain Water
Diffficulty: Hard

Time Complexity: O(n)
Space Complexity: O(1)

"""

class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        left_max, right_max = 0, 0
        total_water = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    total_water += left_max - height[l]
                l+=1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    total_water += right_max - height[r]
                r -=1
        return total_water
