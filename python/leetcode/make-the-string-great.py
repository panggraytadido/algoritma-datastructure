# https://leetcode.com/problems/make-the-string-great/

# Given a string s of lower and upper case English letters.

# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

# 0 <= i <= s.length - 2

# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
# Notice that an empty string is also good.

# Example 1:

# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
# Example 2:

# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same answer. For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""
# Example 3:

# Input: s = "s"
# Output: "s" 

# Constraints:
# 1 <= s.length <= 100
# s contains only lower and upper case English letters.

import re

#1. string to list
# s = "abBAcC"
s = "leEeetcode"
# s = "aaaaaaAb"
# s="s"
s = list(s)
# print(list(s))
# print(len(s))
def search(s):
    panjang_s = len(s)-1
    remove_list=[]
    for i in range(panjang_s):
        current_string = s[i]
        if i<panjang_s:
            next_string=s[i+1]
            if next_string.isupper():
                if current_string==next_string.lower():
                    cur_index = i
                    next_index = i+1
                    remove_list.append(cur_index)
                    remove_list.append(next_index)

    for i in sorted(remove_list, reverse=True):
        del s[i]

    concat_str = "".join(s)
    res = bool(re.search(r'[A-Z]', concat_str))
    if res:
        return search(s)
    elif len(concat_str)>0:
        return concat_str
    else:
        return '""'


print(search(s))

# remove_list = search(s)
# for i in sorted(remove_list, reverse=True):
#     del s[i]

# concat_str  = "".join(s)

# res = bool(re.search(r'[A-Z]', concat_str))
# if res:
#     print('ada')
    
# s1='a'
# s2='A'

# if s2.isupper():
#     print('benar')
# else:
#     print('salah')

# if s1==s2:
#     print('sama')
# else:
#     print('tidak sama')

# s='a'
# d =s.isupper()
# print(d)
# print(remove_list)
# print(next_string)
# print(panjang_s)
