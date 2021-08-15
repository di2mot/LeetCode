'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(strs: list[str]) -> str:

        n = False
        s = ''
        for i in range(len(strs[0])+1):
            for n in strs:
                if strs[0][0:i] == n[0:i]:
                    n = True
                else:
                    n = False 
                    break
            if n: s = strs[0][0:i]
            else: return s
        return s

a = ["flower","flower","flower","flower"]
b = ['']
c = ['a']
d = ["flower","fower","flower","flower"]
e = ["flower","f","ower","flower"]
f = ["c","acc","ccc"]

s = Solution
print(s.longestCommonPrefix(f))
'''
Runtime: 32 ms, faster than 79.71% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.2 MB, less than 82.15% of Python3 online submissions for Longest Common Prefix.
'''