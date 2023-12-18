
s='[}'

def oke(s):
    status=1
    key = ['(','{','[']
    value = [')','}',']']

    string = list(s)

    if len(string)>1:
        for i in range(len(string)):
            if string[i] in key:
                index = key.index(string[i])
                status=1
            else:
                if status==1:
                    if string[i] in value:
                        index_next = value.index(string[i])
                        if index==index_next:
                            status=1
                        else:
                            status=2

                else:
                    status=2
    else:
        status=2
        
    if status==2:
        return False
    elif status==1:
        return True


print(oke(s))