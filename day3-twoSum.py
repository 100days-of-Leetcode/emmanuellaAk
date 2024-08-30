"""
https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the number and its index
        num_dict = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement that we need to find
            complement = target - num
            
            # If the complement exists in the dictionary, return the indices
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # Otherwise, add the number and its index to the dictionary
            num_dict[num] = i

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  
