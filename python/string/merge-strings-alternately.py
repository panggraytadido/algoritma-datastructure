#https://leetcode.com/problems/merge-strings-alternately/

word1 = "abcd" 
word2 = "pqr"

def merge_cross(word1,word2):
    w1 = list(word1)
    w2 = list(word2)

    final_word=[]
    len_w1= len(w1)
    len_w2= len(w2)
    if len_w1==len_w2:
        for i in range(len_w1):
            final_word.append(w1[i])
            final_word.append(w2[i])
    if len_w1<len_w2:
        for i in range(len_w2):
            if i < len_w1: 
                final_word.append(w1[i])
            final_word.append(w2[i])
    if len_w1>len_w2:
        for i in range(len_w1):
            final_word.append(w1[i])
            if i < len_w2: 
                final_word.append(w2[i])

    return ''.join(final_word)


print(merge_cross(word1,word2))
