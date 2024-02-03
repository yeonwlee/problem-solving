#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
#https://yeonwlee.github.io/posts/problemsolving-leetcode-28-find-the-index-of-the-first-occurrence-in-a-string/

#제출한 답
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

#find 구현(슬라이싱 없이)
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        return self._find(haystack, needle)
    
    def _find(self, haystack: str, needle: str) -> int:
        needle_index = 0
        start_index_same_char = 0
        for index in range(len(haystack) - len(needle) + 1):
            haystack_index = index     
            while haystack[haystack_index] == needle[needle_index]:
                if needle_index == 0:
                    start_index_same_char = index
                needle_index += 1
                haystack_index += 1
                if needle_index == len(needle):
                    return start_index_same_char
            needle_index = 0
        return -1

#구현 find 개선
class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        return self._find(haystack, needle)

    def _find(self, haystack: str, needle: str) -> int:
        for index in range(len(haystack) - len(needle) + 1):
            needle_index = 0
            haystack_index = index
            start_index_same_char = index
            while haystack[haystack_index] == needle[needle_index]:
                needle_index += 1
                haystack_index += 1
                if needle_index == len(needle):
                    return start_index_same_char
        return -1