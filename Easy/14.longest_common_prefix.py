'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(strs: list[str]) -> str:
        s = ''
        for i in strs[0]:
            n = 0
            s += i 
            for x in strs:
                if s in x:
                    n += 1
                    #print(s, x, n)
            print(n)
            if n != len(strs):
                return s[:-1]
            elif n == 1 :
                return '0'





x = ["flower","flow","light"]

s = Solution
print(s.longestCommonPrefix(x))
