"""
leetcode 22 - Generate parentheses
Difficulty: Medium
Time comp: O(2 ** n)
Space comp: O(n)
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        sol = []
        def backtrack(openn, close):
            if len(sol) == n * 2:
                ans.append("".join(sol))
                return
            if openn < n:
                sol.append('(')
                backtrack(openn +1, close)
                sol.pop()
            if openn > close:
                sol.append(')')
                backtrack(openn, close + 1)
                sol.pop()
        backtrack(0, 0)
        return ans
