"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type.

"""

"""
Use a stack to store the opening brackets as we iterate through the string. If a closing bracket is encountered, we check if the corresponding opening bracket is at the top of the stack. If it is, we pop the opening bracket off the stack. If not, or if the stack is empty, we return False. Finally, we return the result of a check whether the stack is empty or not.
"""


def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack