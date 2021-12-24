"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""

input = 1234321
arrInput = []
def transIntToArr(intInput, arrOutput):
    """
    use mod and recursive to trans int to array
    """
    modInt = int(intInput % 10)
    arrOutput.insert(0, modInt)
    leftInt = int((intInput - modInt)/10)
    if leftInt > 10:
        transIntToArr(leftInt, arrOutput)
    else:
        arrOutput.insert(0, leftInt)
        return arrOutput

def isPalin(arrInput):
    increseFlag = 1
    for i, val_i in enumerate(arrInput):        
        if increseFlag == 1:
            compareValue = arrInput[i+1] - arrInput[i]
            ##print(i, arrInput[i] , arrInput[i+1])
        else:
            compareValue = arrInput[i] - arrInput[i-1]
            ##print(i, arrInput[i] , arrInput[i-1])
        if compareValue == 1 and increseFlag == 1:
            continue
        elif compareValue == -1 and increseFlag == 0:
            continue
        elif compareValue == -1 and increseFlag == 1:
            increseFlag = 0
            continue
        else:
            return False
    return True

transIntToArr(input, arrInput)
##print(arrInput)

reverseInt = 0
for i, val_i in enumerate(arrInput): 
    reverseInt = 10*reverseInt + arrInput[len(arrInput)-1-i]

if isPalin(arrInput) == True and reverseInt == input and input > 0:
    print("pass")
else:
    print("fail")
