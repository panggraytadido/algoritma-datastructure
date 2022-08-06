#https://leetcode.com/problems/find-first-palindromic-string-in-the-array/ 

from inspect import indentsize


words = ["abc","car","ada","racecar","cool"]
words=["def","ghi"]

palindrome=''
j=0
for strs in words:
    s = list(strs)
    start = len(s)-1
    for i in range(start, -1, -1): #O(n)
        palindrome = palindrome+s[i] #O(1)

    if strs==palindrome:
        print(strs)
        break
    else:
        if j==len(words)-1:
            print('not ok')
            break
        

    j+=1
    palindrome=''
