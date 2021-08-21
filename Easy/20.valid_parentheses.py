'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''


class Solution:
    def isValid(s: str) -> bool:
        a = {
            '(': ')',
            '{': '}',
            '[': ']',
            }
        stuck = []
        for i in s:
            if i in a:
                stuck.append(a[i])
            else:
                if not stuck: return False
                if i == stuck[-1]:
                    stuck.pop()
                else: return False
        if stuck: return False
        else: return True



a = [
    '()',
    "()[]{}",
    '((})[]',
    "(]",
    "([)]",
    '{[()]}',
    "(){}}{",
    '[',
    ']]',
    '[[',
    "({{{{}}}})",
    "(([]){})"
    ]

s = Solution
for n in a:
    print('Task: ', n,  'Resolt: ',s.isValid(n))

'''
Runtime: 24 ms, faster than 95.45% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.2 MB, less than 64.79% of Python3 online submissions for Valid Parentheses.
'''