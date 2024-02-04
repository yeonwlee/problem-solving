#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
#https://yeonwlee.github.io/posts/problemsolving-leetcode-1047-remove-all-adjacent-duplicates-in-string/

#제출한 답
class Solution:
    def removeDuplicates(self, source: str) -> str:
        stack = []
        for index, char in enumerate(source):
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
        
        
## 만약 모든 연속된 문자열을 제거하려고 한다면? 
class Solution2:
    def removeDuplicates(self, source: str) -> str:
        stack = []
        is_dupled = False
        index = 0
        while index < len(source):
            if stack and stack[-1] == source[index]:
                is_dupled = True
            else:
                if is_dupled:
                    stack.pop()
                    is_dupled = False
                    continue
                stack.append(source[index])
            index += 1
        if is_dupled:
            stack.pop()
        return ''.join(stack)
    