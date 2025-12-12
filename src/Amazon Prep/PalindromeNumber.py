# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        reversed = 0
        while x > reversed:
            reversed = reversed * 10 + x % 10 
            x = x // 10
        if x == reversed:
            return True
        if x == reversed // 10:
            return True
        else:
            return False