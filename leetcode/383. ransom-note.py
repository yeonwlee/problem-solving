#https://leetcode.com/problems/ransom-note/
from collections import defaultdict

## 굳이 ransomnote의 문자 수를 세 놓을 딕셔너리를 만들 필요가 없음
# class Solution:
#     def canConstruct(self, ransomnote: str, magazine: str) -> bool:
#         magazine_char_count = defaultdict(int)
#         ransomnote_char_count = defaultdict(int)
#         for char in magazine:
#             magazine_char_count[char] += 1
#         for char in ransomnote: 
#             ransomnote_char_count[char] += 1
#         for char in ransomnote_char_count.keys():
#             if magazine_char_count[char] < ransomnote_char_count[char]:
#                 return False
#         return True

class Solution:
    def canConstruct(self, ransomnote: str, magazine: str) -> bool:
        magazine_char_count: dict[str, int] = defaultdict(int)
        for char in magazine:
            magazine_char_count[char] += 1
        for char in ransomnote:
            if magazine_char_count[char] == 0:
                return False
            magazine_char_count[char] -= 1
        return True