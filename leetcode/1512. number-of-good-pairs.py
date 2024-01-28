from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        answer = 0
        for num in nums:
            if num in seen:
                answer += seen[num]
            seen[num] += 1
        return answer
        