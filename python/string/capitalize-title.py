#https://leetcode.com/problems/capitalize-the-title/

str = "First leTTeR of EACH Word"
str = "First leTTeR"
def cap(str):
    str = str.split(" ")
    final_str = []
    for i in str: 
        if len(i) > 2:
            before = i[0].lower()
            after = i[0].upper()
            lower = i.lower()
            out = lower.replace(before, after,1)
        else:
            out = i.lower()

        final_str.append(out)
    return ' '.join(final_str)
    
     
print(cap(str)) 


# str = 'python'
# print(str[1:])
# print(str.replace("p", "P",1))
