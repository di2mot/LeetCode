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
            ')': False,
            '}': False,
            ']': False,
        }
        x = False
        if len(s) % 2 != 0:
            return False

        for n in range(int(len(s) / 2)):
            if a[s[n]] == s[-(1 + n)]:
                x = True
            else:
                x = False
                break
        if x:
            return x

        for n in range(0, len(s), 2):
            # print(s[n], s[n + 1])
            if a[s[n]] == s[n + 1]:
                x = True
            else:
                x = False
                break
        if x:
            return True
        return False


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
    "({{{{}}}))",
    "(([]){})"
    ]

s = Solution
for n in a:
    print('Task: ', n,  'Resolt: ',s.isValid(n))
