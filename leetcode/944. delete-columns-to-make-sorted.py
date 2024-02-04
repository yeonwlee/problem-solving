#https://leetcode.com/problems/delete-columns-to-make-sorted/
#https://yeonwlee.github.io/posts/problemsolving-leetcode-944-delete-columns-to-make-sorted/

## 1
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columns = zip(*strs)
        return sum(1 if sorted(col) != list(col) else 0 for col in columns)

## 2
class Solution2:
    def minDeletionSize(self, strs: List[str]) -> int:
        num_of_del_cols = 0
        for col_index in range(len(strs[0])):
            for row_index in range(len(strs) - 1):
                if strs[row_index][col_index] > strs[row_index + 1][col_index]:
                    num_of_del_cols += 1
                    break
        return num_of_del_cols