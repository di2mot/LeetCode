'''
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 3:
            return s[0]

        stuck = []
        n = 0
        t_n = 0
        t = False

        for x in range(len(s)):
            for y in range(len(s)-1, x, -1):
                
                if s[x] == s[y]:
                    print(f'x={x}, s[x]={s[x]}, y={y}, s[y]={s[y]}')
                    t = True

                    if y - x == 2:
                        t_n += 3
                    else:
                        t_n += 2

                    if n < t_n: 
                        n = t_n
                    break
                else:
                    t = False
                    t_n = 0
        return n


a = 'baabad'
s = Solution()
b = s.longestPalindrome(a)
print(b)