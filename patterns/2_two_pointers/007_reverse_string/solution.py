"""
# leetcode 344
Difficulty : Easy

Time complexity : O(n)
Space complexity : O(1)

"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        n = len(s)

        l, r = 0, n-1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1