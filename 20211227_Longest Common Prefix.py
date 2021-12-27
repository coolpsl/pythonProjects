"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
input_strs= ["aaadog","aaaracecar","aaacar"]

matrix_input = []
outPrefix = ""
minLen = 200
inputSize = len(input_strs)

for strs in input_strs:
    matrix_input.append(list(strs))
    if len(strs) < minLen:
        minLen = len(strs)

##print("min string length : ", minLen, "Input Array Size : ", inputSize)

for i in range(0,minLen):
    tempChar = matrix_input[0][i]
    diffFlag = False
    for j in range(1, inputSize):
        if tempChar != matrix_input[j][i]:
            diffFlag = True
    if not diffFlag:
        outPrefix += tempChar

print("input array : ",input_strs)
print("output prefix : ",outPrefix)
