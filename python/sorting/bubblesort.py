arr = [4,6,2,7,8,4,5,100,45]

a=1
count = len(arr)
for i in range(count):
   for j in range(count-a):
       if arr[j] > arr[j+1]:
            t = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = t;
            
a+=1

print(arr)