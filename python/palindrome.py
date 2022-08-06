
string = 'batab'

def check_palindrome(s):
    s = list(string)
    start = len(s)-1
    palindrome = ''
    for i in range(start, -1, -1): #O(n)
        palindrome = palindrome+string[i] #O(1)

    if palindrome==string:
        return 'palindrome'
    else:
        return 'not palindrome'

print(check_palindrome(string))



