#https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for index, first_number in enumerate(nums):
            for second_number in nums[index + 1:]:
                if first_number + second_number >= target:
                    break
                count += 1 
        return count
    
    def countPairs2(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        left_pointer, right_pointer = 0, len(nums) - 1
        while left_pointer < right_pointer:
            if nums[left_pointer] + nums[right_pointer] < target:
                count += (right_pointer - left_pointer)
                left_pointer += 1
            else:
                right_pointer -= 1
        return count