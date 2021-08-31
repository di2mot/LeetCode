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
        if numRows == 1: return s

        res = ''

        for line in range(numRows):
            inc = numRows+(numRows-2)
            for i in range(line, len(s), inc):
                res += s[i]
                if (line > 0 and line < numRows - 1 and
                i + inc - 2 * line < len(s)):
                    res += s[i + inc - line * 2]

        return res
        



e = "PAYPALISHIRING"
a = 'ABCDEFGHIJKLMNOPQR'
numRows = 4
s = Solution()
b = s.convert(e, numRows)
print(b)

'''
Runtime: 80 ms, faster than 27.04% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 14.3 MB, less than 70.79% of Python3 online submissions for ZigZag Conversion
'''