#https://leetcode.com/problems/valid-parentheses/
#https://yeonwlee.github.io/posts/problemsolving-leetcode-20-valid-parentheses/

## 중첩 괄호 가능성 배제시
class Solution:
    def isValid(self, parentheses: str) -> bool:
        brackets: dict[str, str] = {'(': ')', '{': '}', '[':']'}
        if len(parentheses) % 2 == 1:
            return False
        for index in range(0, len(parentheses) - 1, 2):
            if parentheses[index] not in brackets:
                return False
            if parentheses[index + 1] != brackets[parentheses[index]]:
                return False
        return True

## 중첩 괄호 가능성 고려시
class Solution2:
    def isValid(self, parentheses: str) -> bool:
        close_brackets = {')': '(', '}': '{', ']':'['}
        if len(parentheses) % 2 == 1:
            return False
        stack: list[str] = []
        for index, char in enumerate(parentheses):
            if char in close_brackets:
                if not stack or stack.pop() != close_brackets[char]:
                    return False
            else:
                stack.append(char)
        return not stack ## 모두 비어있으면 True