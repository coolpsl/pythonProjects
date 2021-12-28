"""
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

list1 = [1,2,3,3,5]
list2 = [2,3,4]
listLen1 = len(list1)
listLen2 = len(list2)
outputList = []
idx1 = 0
idx2 = 0

while idx1 < listLen1 and idx2 < listLen2:
    if list1[idx1] < list2[idx2]:
        outputList.append(list1[idx1])
        idx1 = idx1 + 1
    else:
        outputList.append(list2[idx2])
        idx2 = idx2 + 1

if  list1[listLen1-1] > list2[listLen2-1]:   
    outputList.append(list1[listLen1-1])   
else:
    outputList.append(list2[listLen2-1])   

print(outputList)