#create kotak
def kotak(l):
    for i in range(l):
        for j in range(l): 
            if i!=0 and i!=l-1:
                if j==0 or j==l-1:
                    print("*",end="    ")
                else:
                    print(end=" ")
            else:
                print("*",end=" ")
        print(" ")
    return ""

#create angka 7
def tujuh(l):
    for i in range(l):
        for j in range(l): 
            if i==0:
                print("*",end=" ")
            else:
                column = l-i
                if column==j:
                    print("*",end=" ")
                else:
                    print(end="  ")
        print(" ")
    return ""

#create diagonal left
def diagonal_left(l):
    for i in range(l):
        for j in range(l):
            if i==j:
                print("*",end="")
            else:
                print(end=" ")

        print("")
    return ""

#create diagonal left
def diagonal_left(l):
    for i in range(l):
        for j in range(l):
            column = l-i
            if column==j:
                print("*",end=" ")
            else:
                print(end=" ")
        
        print(" ")
    return ""

#create rectangle left
def segitiga_left(l):
    for i in range(l):
        for j in range(0,i+1):
            print("*",end=" ")
        print(" ")
    return ""

def huruf_l(l):
    max = l-1
    for i in range(l):
        for j in range(l):
            if j==0:
                print("*",end=" ")
            elif j>0 and i==max:
                print("*",end=" ")
        print(" ")
    return ""

def huruf_n(l):
    max = l-1
    for i in range(l):
        for j in range(l):
            if j==0 or j==max:
                print("*",end=" ")
            else:
                if i==j:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        print(" ")
    return ""


def huruf_k(l):
    mid = l // 2
    # print(mid)
    for i in range(l):
        for j in range(l):
            if j==0:
                print("*",end=" ")
            else:
                if j<4:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        print(" ")
    return ""


# print(kotak(15))
# print(huruf_k(5))
