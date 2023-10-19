
#https://leetcode.com/problems/valid-parentheses/
status=1
key = ['(','{','[']
value = [')','}',']']

string = "{[]}("
# string = '()'
string = list(string)

if len(string)>1:
    for i in range(len(string)):
        if string[i] in key:
            index = key.index(string[i])
            # print('index : '+str(index))
            status=1
        else:
            if status==1: 
                if string[i] in value:
                    index_next = value.index(string[i])
                    # print('indexnex : '+str(index_next))
                    # if index==index_next:
                    #     status=1
                    # else:
                    #     status=2
            # else:
            #     status=2
else:
    status=2


print(status)