'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        up = ''
        dwn = ''
        ent = ''
        for i in range(0, len(s), 4):
            up += s[i]
        for i in range(2, len(s), 4):
            dwn +=s[i]
        for i in range(0, len(s)):
            if s[i] not in up and s[i] not in dwn:
                ent += s[i]

        print(up +ent + dwn)
        



e = "PAYPALISHIRING"
a = 'ABCDEFGHIJKLMNOPQR'
numRows = 3
s = Solution()
b = s.convert(a, numRows)
print(b)