"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
a = "1010"
b = "1011"
ret = []

maxLen = len(a) if len(a)>len(b) else len(b)
carryFlag = False
for i in range(maxLen):
    indexA = int(a[len(a)-1-i]) if len(a) > i else 0
    indexB = int(b[len(b)-1-i]) if len(b) > i else 0
   
    if carryFlag:
        result = indexA + indexB +1 
        carryFlag = False
    else:
        result = indexA + indexB

    if result > 1:
        carryFlag = True
        result = result % 1

    ret.insert(0, result)

if carryFlag:
   ret.insert(0, 1) 
strRet = ''.join(str(e) for e in ret)
print(strRet) 