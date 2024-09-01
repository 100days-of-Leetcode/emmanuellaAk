"""
https://leetcode.com/problems/top-k-frequent-elements/description/

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""

from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        
      
        most_frequent = heapq.nlargest(k, count.keys(), key=count.get)
        
        return most_frequent
    
solution = Solution()


nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print("Test case 1: " + str(solution.topKFrequent(nums1, k1)))