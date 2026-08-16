"""
#leetcode 278 - First Bad Version
Difficulty : Easy

Time complexity : O(log n)
Space complexity : O(1)

"""



# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l < r:

            m = (l+r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l