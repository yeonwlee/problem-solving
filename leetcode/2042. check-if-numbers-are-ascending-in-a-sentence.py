#https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
#https://yeonwlee.github.io/posts/problemsolving-leetcode-2042-check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, sentence: str) -> bool:
        numbers = [int(word) for word in sentence.split() if word.isnumeric()]
        previous_num = float('-inf') #조건으로 보아, 0으로 초기화해도 됨
        for num in numbers:
            if num <= previous_num:
                return False
            previous_num = num
        return True