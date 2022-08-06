#https://www.geeksforgeeks.org/find-the-missing-number/
arr = [1, 2, 3, 4,5,6,7,9]
n=8

#dido
#time complexity  # O(n)
def my_func_to_solve(arr,n):
    count = len(arr)-1
    for i in range(count):
        if arr[i]+1!=arr[i+1]:
            return arr[i]+1
            break

def getMissingNo(arr, n):
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(arr)
    return total - sum_of_A

# Python3 program to check missingNo

# Function to find the missing number
def getMissingNo2(arr, n) :
	i = 0;
	
	while (i < n) :
		# as array is of 1 based indexing so the
		# correct position or index number of each
		# element is element-1 i.e. 1 will be at 0th
		# index similarly 2 correct index will 1 so
		# on...
		correctpos = arr[i] - 1;
		if (arr[i] < n and arr[i] != arr[correctpos]) :
			# if array element should be lesser than
			# size and array element should not be at
			# its correct position then only swap with
			# its correct position or index value
			arr[i],arr[correctpos] = arr[correctpos], arr[i]

		else :
			# if element is at its correct position
			# just increment i and check for remaining
			# array elements
			i += 1;
			
	# check for missing element by comparing elements with their index values
	for index in range(n) :
		if (arr[index] != index + 1) :
			return index + 1;
			
	return n;

print(my_func_to_solve(arr,n))