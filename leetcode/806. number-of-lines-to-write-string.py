import string


###실수1 문제를 잘못 이해함.
###+굳이 내림차순으로 정렬할 필요도, while로 돌면서 pop할 필요 없었다. 이해한 바 대로 풀어도 그냥 오름차순 정렬에 순회로 했어도 됐다.
def number_of_lines(widths, sentence):
    count_of_lines = 1
    width_info = _make_width_info(widths, string.ascii_lowercase)
    sorted_sentence_by_width = sorted(list(sentence), key=lambda x: width_info[x], reverse=True)
    cur_line_width = 0
    while sorted_sentence_by_width: 
        cur_char = sorted_sentence_by_width[-1]
        if cur_line_width + width_info[cur_char] <= 100:
            cur_line_width += width_info[cur_char]
        else:
            count_of_lines += 1
            cur_line_width = width_info[cur_char]
        sorted_sentence_by_width.pop()    
    return [count_of_lines, cur_line_width]
def _make_width_info(widths, charset_info):
    width_info = {}
    for index, character in enumerate(charset_info):
        width_info[character] = widths[index]
    return width_info


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