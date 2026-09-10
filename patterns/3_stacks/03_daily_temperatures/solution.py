"""
# leetcode 739
Difficulty : Medium
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        temps = temperatures
        n = len(temps)
        answer = [0] * n
        stk = []
 
        for i, t in enumerate(temps):
            while stk and stk[-1][0] < t:
                stk_t, stk_i = stk.pop()
                answer[stk_i] = i - stk_i
 
            stk.append((t, i))
        return answer

 
