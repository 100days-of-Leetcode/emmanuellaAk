"""
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
https://leetcode.com/problems/valid-palindrome/description/
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        filtered_chars = ''.join(char.lower() for char in s if char.isalnum())
        
       
        return filtered_chars == filtered_chars[::-1]
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  
print(solution.isPalindrome("race a car"))  



