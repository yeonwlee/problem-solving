#https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/
#https://yeonwlee.github.io/posts/problemsolving-leetcode-2586-count-the-number-of-vowel-strings-in-range/

#제출한 답
class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return len([word for word in words[left:right + 1] if word[0] in vowels and word[-1] in vowels])

#고려해 볼 수 있는 사항
class Solution2:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for index in range(left, right + 1):
            word = words[index]
            if word[0] in vowels and word[-1] in vowels:
                count += 1
        return count