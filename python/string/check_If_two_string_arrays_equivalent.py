#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

word1 = ["ab", "cd"]
word2 = ["a", "bc"]

w1 = ''.join(word1)
w2 = ''.join(word2)

if w1==w2:
    print('ok')
else:
    print('not ok')
