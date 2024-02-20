
#https://leetcode.com/problems/robot-return-to-origin/
#https://yeonwlee.github.io/posts/problemsolving-leetcode-657-robot-return-to-origin/

from collections import Counter

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) % 2 == 0:
            result: Counter = Counter(moves)
            return result['R'] == result['L'] and result['U'] == result['D']
        return False
  
class Solution2:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) % 2 == 0:
            result: Counter = Counter(moves)
            return result['R'] - result['L'] == 0 and result['U'] - result['D'] == 0
        return False