"""
#leetcode 11. Container With Most Water

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

"""
class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        L, R = 0, n - 1
        max_area = 0
        while L < R:
            area = min(height[L], height[R]) * (R - L)
            max_area = max(max_area, area)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return max_area 
