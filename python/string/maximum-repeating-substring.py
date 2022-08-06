#https://leetcode.com/problems/maximum-repeating-substring/

sequence='a'
word='a'

sequence="aaabaaaabaaabaaaabaaaabaaaabaaaabaaaaba"
word="aaaba"


def max_repeating_substring(sequence,word):
    sequence = list(sequence)
    total=0
    len_word = len(word)
    start=0
    end=len_word
    compare=''
    for i in range(len(sequence)):
        compare=''
        for j in range(start,end,1):
            if j < len(sequence): 
                compare +=sequence[j]
        start+=1
        end+=1

        if compare==word:
            total = total+1
        
    return total
    
print(max_repeating_substring(sequence,word))
    
        

# start=1
# end=4
# for i in range(start,end,1): #O(n)
#         print(i)

    # compare = str(sequence[i]+sequence[i+1])
    # print(sequence[i])
    # if compare==word:
    #     total=total+1



# print(compare)