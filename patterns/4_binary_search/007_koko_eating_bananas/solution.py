"""
# leetcode problem link: https://leetcode.com/problems/koko-eating-bananas/
# leetcode 875. Koko Eating Bananas

Difficulty: Medium

Time Complexity: O(n log m).
Space Complexity: O(1).

"""

import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        def k_works(k):
            hours = 0 

            for p in piles:
                hours += math.ceil(p / k)

            return hours <= h

        l = 1
        r = max(piles)

        while l < r:
            k = (l+r) // 2

            if k_works(k):
                r = k
            else:
                l = k+1

        return r