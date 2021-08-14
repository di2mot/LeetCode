'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.
'''

class Solution:
    def isPalindrome(x: int) -> bool:
        n = 1
        y = str(x)
        for i in range(len(y)):
            if y[i] != y[-n]:
                return False
            n += 1
        return True

x = 10

s = Solution
print(s.isPalindrome(x))