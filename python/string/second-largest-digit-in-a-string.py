#https://leetcode.com/problems/second-largest-digit-in-a-string/

from curses.ascii import isdigit


s = "dfa12321afd"

str = ''
for i in s:
    if i.isdigit():
        str = str + i

digit = list(str)
max = digit[0]
for i in digit:
    if int(i)>int(max):
        max = i
        break
    else:
        max=0

if max==0:
    print('-1')

else:
    print(max)