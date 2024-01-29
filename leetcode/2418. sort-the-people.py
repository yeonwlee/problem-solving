#https://leetcode.com/problems/sort-the-people/
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [info[0] for info in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)]
        