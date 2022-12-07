""" 
Write a function to find the longest common prefix string amongst an array of strings.
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

strs = ["flower","flow","flight"]

m = ''
flag = 1
j = 0
while flag == 1:
     count = 0
     temp = strs[0][j]
     for i in range(0,len(strs)):
          if strs[i][j] == temp:
               count += 1

     if count == len(strs):
          j = j + 1
     else:
          flag = 0

m = strs[0][0:j]
print(m)
