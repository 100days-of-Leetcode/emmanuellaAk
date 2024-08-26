"""
Two Sum
https://leetcode.com/problems/contains-duplicate/description/

Problem description :
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""
from typing import List
#solution
class Solution:
  def hasDuplicate(self, nums: List[int]) -> bool:
  #set to store elements that have checked so far in the loop
   elements = set();

   for num in nums:
     #add elements that have been checked to the set
     elements.add(num)
     #check for duplicate
     if num in elements:
         return True
   return False

solution = Solution()
#test case
print(solution.hasDuplicate([1,5,3,2,1]))