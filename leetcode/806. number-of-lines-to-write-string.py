import string

# def number_of_lines(widths, sentence):
#     #dict를 만들면 좋을 것 같다.
#     count_of_lines = 1
#     width_info = _make_width_info(widths, string.ascii_lowercase)
#     #그리고 정렬. 앞에서부터 수를 꺼내면, 배열 요소를 움직여줘야하니 뒤에서 뽑자.
#     sorted_sentence_by_width = sorted(list(sentence), key=lambda x: width_info[x], reverse=True)
#     cur_line_width = 0
#     while sorted_sentence_by_width:
#         cur_char = sorted_sentence_by_width[-1]
#         if cur_line_width + width_info[cur_char] <= 100:
#             cur_line_width += width_info[cur_char]
#             sorted_sentence_by_width.pop()
#         else:
#             count_of_lines += 1
#             cur_line_width = 0
#     return [count_of_lines, cur_line_width] 
# def _make_width_info(widths, charset_info):
#     width_info = {}
#     for index, character in enumerate(charset_info):
#         width_info[character] = widths[index]
#     return width_info


###실수1 문제를 잘못 이해함. 주어진 문자의 순서는 그대로여야했다.
class Solution:
    def _make_width_info(self, widths, charset_info):
        width_info = {}
        for index, character in enumerate(charset_info):
            width_info[character] = widths[index]
        return width_info
    def numberOfLines(self, widths: List[int], sentence: str) -> List[int]:
        #dict를 만들면 좋을 것 같다.
        width_info = self._make_width_info(widths, string.ascii_lowercase)
        count_of_lines = 1
        cur_line_width = 0
        for cur_char in sentence:
            if cur_line_width + width_info[cur_char] <= 100:
                cur_line_width += width_info[cur_char]
            else:
                count_of_lines += 1
                cur_line_width = width_info[cur_char]
        return [count_of_lines, cur_line_width] 