arr=[3,4,5,6,7,8,1,2]
s=arr[0]

count=len(arr)-1
for i in range(count):
    if arr[i]<s:
        s=arr[i]
        
        # print(arr[i])
        # break

print(s)
# print(arr)