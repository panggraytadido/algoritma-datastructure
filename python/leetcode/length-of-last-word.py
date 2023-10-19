s = "Hello World 13  "
# s = "   fly me   to   the moon  "

string = list(s.split(" "))
count = len(string)-1

for i in range(count,-1,-1):
    if len(string[i])>0:
        print(len(string[i]))
        break