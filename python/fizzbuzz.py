
def fizzbuzz(n):
    out=''
    list_nya=[]
    n=n+1
    for i in range(1,n):
        if i%3==0 and i%5==0:
            out='FizzBuzz'
        elif i%3==0:
            out='Fizz'
        elif i%5==0:
            out ='Buzz'
        else:
            out= str(i)

        list_nya.append(out)


print(fizzbuzz(4))


