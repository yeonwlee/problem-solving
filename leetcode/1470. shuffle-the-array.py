#https://leetcode.com/problems/shuffle-the-array/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for cur_tuple in zip(nums[:n], nums[n:]):
            answer.append(cur_tuple[0])
            answer.append(cur_tuple[1])
        return answer