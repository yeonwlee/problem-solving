#https://leetcode.com/problems/long-pressed-name/

## 제출한 답
# def is_long_pressed_name(name: str, typed: str) -> bool:
#     if name == typed:
#         return True
#     if len(name) < len(typed):
#         gen_cur_name_char = generator_for_getting_name_char(name)
#         cur_name_char = next(gen_cur_name_char)
#         pre_same_char: str = ''
#         for cur_typed_index, cur_typed_char in enumerate(typed):
#             if cur_name_char == cur_typed_char:
#                 pre_same_char = cur_name_char
#                 try:
#                     cur_name_char = next(gen_cur_name_char)
#                 except StopIteration:
#                     for last in typed[cur_typed_index:]:
#                         if last != cur_name_char:
#                             return False
#                     return True
#             else:
#                 if cur_typed_char != pre_same_char:
#                     return False 
#     return False

# def generator_for_getting_name_char(name: str):
#     for cur_name_char in name:
#         yield cur_name_char

## 개선 코드
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_index, typed_index = 0, 0

        while typed_index < len(typed):
            if name_index < len(name) and name[name_index] == typed[typed_index]:
                name_index += 1
            elif typed_index == 0 or typed[typed_index] != typed[typed_index - 1]:
                return False
            typed_index += 1

        return name_index == len(name)

