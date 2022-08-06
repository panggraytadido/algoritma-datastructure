arr = [1,2,199] # [1,2,4]

# [2,3,4] return [2,3,5]

last_element = len(arr)-1
value = arr[last_element] +1
arr[last_element] = value
print(arr)