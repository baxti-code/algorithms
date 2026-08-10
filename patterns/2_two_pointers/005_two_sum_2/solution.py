"""
#167 leetcode - "Two sum 2"
Difficulty : Medium

Time complexity : O(n)
Space Complexity : O(1)

"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        l, r = 0, n-1
        while l < r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l +1 , r+1]
            elif summ > target:
                r -= 1
            else:
                l += 1
