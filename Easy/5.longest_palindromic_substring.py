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
            if s[0] != s[-1]:
                return s[0]
            else: return s
        elif len(s) == s.count(s[0]):
            return s

        start = 0
        stop = 0
        max_len = 0

        def recurs_checker(s: str) -> bool:
            if len(s) <= 1:
                return True
            if s[0] == s[-1]:
                return recurs_checker(s[1:-1])
            else: return False

        for x in range(len(s)):
            for y in range(len(s)-1, x, -1):
                if s[x] == s[y]:

                    # print(x, y)
                    # print(s[x:y+1], len(s[x:y+1]), len(s[x:y+1])//2)
                    temp = s[x:y+1]

                    if len(temp) == 3:
                        left = temp[0: 1]
                        right = temp[1: -1]
                        # print('2',temp, left,right, x, y, right[::-1])

                    if len(temp) == 2:
                        left = temp[0]
                        right = temp[1]
                        # print('2',temp, left,right, x, y, right[::-1])

                    elif len(temp)%2 == 0 and len(temp) > 2:
                        left = temp[0:(len(temp)//2)]
                        right = temp[(len(temp)//2): len(temp)]
                        print('0',left, right[::-1])

                    else:
                        left = temp[0:(len(temp)//2)+1]
                        right = temp[(len(temp)//2): len(temp)]
                        print('1', temp,x,y, left, right[::-1])

                    if left == right[::-1]:

                        if len(s[x:y+1]) > max_len:
                            max_len = len(temp)
                            start = x
                            stop = y + 1
        if len(s[start:stop]):
            return s[start:stop]
        else: return s[0]


a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
e = "abcda"
s = Solution()
b = s.longestPalindrome(e)
print(b)

'''
Runtime: 7629 ms, faster than 14.26% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.3 MB, less than 82.93% of Python3 online submissions for Longest Palindromic Substring.
'''