#1 by using set() (optimal)

class Solution:
    def containsDuplicate(self, nums:list [int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False



#2 using counter
# from collections import Counter
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         h = Counter(nums)
#         for key, value in h.items():
#             if value > 1:
#                 return True
#         return False


    