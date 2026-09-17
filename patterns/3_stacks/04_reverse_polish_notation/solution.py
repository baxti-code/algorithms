"""
leetcode 150 - Reverse Polish notation
Difficulty : Medium
Time complexity: O(n)
Space complexity: O(n)
"""

from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stk = []
        for t in tokens:
            if t in '+-*/':
                b, a = stk.pop(), stk.pop()
                if t == '-':
                    stk.append(a-b)
                elif t == '+':
                    stk.append(a+b)
                elif t == '*':
                    stk.append(a*b)
                else:
                    division = a/b
                    if division > 0:
                        stk.append(floor(division))
                    else:
                        stk.append(ceil(division))
            else:
                stk.append(int(t))

        return stk[0]