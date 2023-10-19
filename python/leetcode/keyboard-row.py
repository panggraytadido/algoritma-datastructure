#https://leetcode.com/problems/keyboard-row/

# a = ['q','w','e','r','t','y','u','i','o','p']
# b = ['a','s','d','f','g','h','j','k','l']
# c = ['z','x','c','v','b','n','m']

words = ["Hello","Alaska","Dad","Peace","nm"] 

# for str in words:
#     print(str)

a=set("qwertyuiop")
b=set("asdfghjkl")
c=set("zxcvbnm")
res=[]
for word in words:
    if set(word.lower()).issubset(a):
        res.append(word)
    elif set(word.lower()).issubset(b):
        res.append(word)
    elif set(word.lower()).issubset(c):
        res.append(word)

print(res)