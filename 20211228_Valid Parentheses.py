"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

inputStr = "()}]"
arrInput = list(inputStr)
strLen = len(inputStr)
errFlag = 0

def charCompare(char1, char2):
    if char1 == '(' and char2 ==')':
        return True
    if char1 == '[' and char2 ==']':
        return True
    if char1 == '{' and char2 =='}':
        return True
    else:
        return False

for i in range(0,int(strLen/2)):
    if not charCompare(arrInput[2*i], arrInput[2*i+1]):
        print("false")
        errFlag = 1
if not errFlag:
    print("true")