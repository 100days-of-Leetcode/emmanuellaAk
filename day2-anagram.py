"""
Valid Anagram
https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
#Solution

class Solution:
  def isAnagram(self, s:str, t:str) ->bool:
    return len(s) == len(t) and sorted(s) == sorted(t)

solution = Solution()
print(solution.isAnagram('qwetrty','wretyq'))