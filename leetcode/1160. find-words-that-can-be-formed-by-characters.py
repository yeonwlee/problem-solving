#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
#https://yeonwlee.github.io/posts/problemsolving-leetcode-1160-find-words-that-can-be-formed-by-characters/
from collections import Counter
import copy

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_counter = Counter(chars) # O(n) n은 chars의 길이
        num_of_can_be_formed = 0
        for word in words: #O(m) m은 words의 길이
            if self._is_all_in_chars(word, copy.deepcopy(char_counter)): # deepcopy O(u) u는 고유 문자의 수
            # _is_all_in_chars의 순회 O(w) w는 word의 길이
                num_of_can_be_formed += len(word)
        return num_of_can_be_formed

    def _is_all_in_chars(self, word, char_counter):
        for char in word:
            if char in char_counter and char_counter[char] != 0:
                char_counter[char] -= 1
            else:
                return False
        return True
    
## 조금 더 개선
class Solution2:
    def countCharacters(self, words: list[str], chars: str) -> int:
        source_char_counter = Counter(chars) #O(n)
        num_of_can_be_formed = 0
        for word in words: #O(m)
            if self._is_all_in_chars(word, source_char_counter): #O(w)
                num_of_can_be_formed += len(word)
        return num_of_can_be_formed

    def _is_all_in_chars(self, word, source_char_counter):
        word_char_counter = Counter(word) #O(w)
        return source_char_counter > word_char_counter #O(w)