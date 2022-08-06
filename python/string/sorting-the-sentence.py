# https://leetcode.com/problems/sorting-the-sentence/
s = "is2 sentence4 This1 a3"
str = s.split(" ")
kata  = str[0]
dict ={}
for i in str:
    kata  = i
    number = kata[-1]
    kata_exclude_number = kata[:-1]
    dict[number] = kata_exclude_number

dictionary_items = dict.items()
sorted_items = sorted(dictionary_items)
index=0
str=''
list_nya = []
for i in sorted_items:
    list_nya.append(sorted_items[index][1])
    index+=1

d= ' '.join(list_nya)
print(d)
# d = ' '.join(map(str, sorted_items.values()))
# print(d)