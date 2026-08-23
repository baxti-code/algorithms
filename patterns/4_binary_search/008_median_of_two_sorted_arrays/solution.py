"""
# leetcode problem: 4. Median of Two Sorted Arrays
Difficulty: Hard

Time Complexity: O(m + n).
Space Complexity: O(m + n).

"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Merge the two sorted arrays
        merged = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Add remaining elements from nums1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        # Add remaining elements from nums2
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        # Calculate the median
        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0