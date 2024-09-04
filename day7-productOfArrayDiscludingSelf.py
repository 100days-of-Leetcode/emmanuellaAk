"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

https://leetcode.com/problems/product-of-array-except-self/description/
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
        
       
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output
solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  
