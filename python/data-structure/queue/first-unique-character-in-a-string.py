s = "lletcode"

def firstUniqChar(s):
    if len(s)<2:
        return -1
    else:
        length = len(s)-1
        value = s[0]
        for i in range(length):
            for j in range(length):
                if i!=j and value!=s[j]:
                    # print(s[i])
                    print(1)
                    break
                elif i!=j and value==s[j]:
                    value = s[i]

# print(firstUniqChar(s))

def firstUniqChar2(s):
    length = len(s)-1
    for i in range(length):
        next=i+1
        if s[i] in s:
            print('ada')
        else:
            print('tidak')          


print(firstUniqChar(s))