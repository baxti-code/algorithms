"""
#49 leetcode 

Difficulty : Medium
Time comp : O(n · k)
Space comp : O(n · k)

"""


from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] +=1
            
            key = tuple(count)
            groups[key].append(word)
        print(groups)
        return list(groups.values())



# brute force 

# from collections  import defaultdict
# from typing import List

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         d = defaultdict(list)

#         for word in strs:
#             key = ''.join(sorted(word))
#             d[key].append(word)
#         return list(d.values())

# time comp : O(n*k log k)