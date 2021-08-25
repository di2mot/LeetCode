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
                    print(x, y)
                    print(s[x:y+1], len(s[x:y+1]))
                    if len(s[x:y+1])%2 == 0:
                        left = s[x:(len(s[x:y+1])//2)]
                        right = s[(len(s[x:y+1])//2): y+1]
                        print('0',left, right[::-1])

                    else:
                        left = s[x:(len(s[x:y+1])//2)]
                        right = s[(len(s[x:y+1])//2+1): y+1]
                        print('1', left, right[::-1])

                    if left == right[::-1]:

                        if len(s[x:y+1]) > max_len:
                            max_len = len(s[x:y+1])
                            start = x
                            stop = y + 1
                    # else: break

                    # print(f'x={x}, s[x]={s[x]}, y={y}, s[y]={s[y]} {s[x:y+1]}')
                    # if recurs_checker(s[x:y+1]):
                    #     if len(n) < len(s[x:y+1]):
                    #         n = s[x:y+1]
                        # break
        
            # else: continue
        return s[start:stop]


a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
e = 'cbbd'
s = Solution()
b = s.longestPalindrome(e)
print(b)