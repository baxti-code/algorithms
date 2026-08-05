class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = {}
        h2 = {}
        for char in s:
            if char in h:
                h[char]+=1
            else:
                h[char] = 1
        for char in t:
            if char in h2:
                h2[char] +=1
            else:
                h2[char] = 1
        return h == h2
    

#2 using counter 

# from collections import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         s_dict = Counter(s)
#         t_dict = Counter(t)
#         return s_dict == t_dict
    
#time comp: O(n)
#space comp: O(n)