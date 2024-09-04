"""
https://leetcode.com/problems/longest-consecutive-sequence/description/
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Step 1: Create a set of the numbers
        num_set = set(nums)
        
        max_length = 0

        for num in num_set:
          
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
              
                max_length = max(max_length, current_length)
        
        return max_length
solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  
