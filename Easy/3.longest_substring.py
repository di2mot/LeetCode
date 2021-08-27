'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0

dvdf

aab
'''
from datetime import datetime
import time

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = 0
        b = []
        for i in s:
            if i not in b:
                b.append(i)
                if len(b) > n:
                    n = len(b)                
            else:
                b = b[b.index(i)+1:]
                b.append(i)
        return n

a = "aab"

s = Solution()
# b = s.lengthOfLongestSubstring(a)
# print(b)

x = 'byfqe7g8f4buvba89r9348q894thnaaa'
strt = datetime.now()

for i in range(100):
    b = s.lengthOfLongestSubstring(x*i)
    print(i, b, datetime.now() - strt)
'''
Runtime: 68 ms, faster than 53.88% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.2 MB, less than 93.70% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''