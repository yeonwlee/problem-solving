#https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums.sort(reverse=True)
        # return (nums[0]-1) * (nums[1]-1)
        max_value = next_max_value = 0 #조건으로 봤을 때 0보다 작은 수는 없음
        
        for number in nums:
            if number > max_value:
                next_max_value = max_value
                max_value = number
            elif number > next_max_value:
                next_max_value = number
        
        return (max_value-1) * (next_max_value-1)
                
            