#https://leetcode.com/problems/reverse-string/
#https://yeonwlee.github.io/posts/problemsolving-leetcode-344-reverse-string/

## 1
class Solution:
    def reverseString(self, strs: List[str]) -> None:
        strs.reverse()
        
## 2
class Solution2:
    def reverseString(self, strs: List[str]) -> None:
        left, right = 0, len(strs) - 1
        while left < right:
            strs[right], strs[left] = strs[left], strs[right]
            left += 1
            right -= 1
