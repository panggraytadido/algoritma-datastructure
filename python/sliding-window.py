# https://towardsdev.com/sliding-window-algorithm-145f8e201a64
# Window Sliding Technique is a computational technique 
# which aims to reduce the use of nested loop and replace it with a single loop, thereby reducing the time complexity

# What is Sliding Window?

# Consider a long chain connected together. Suppose you want to apply oil in the complete chain with your hands, without pouring the oil from above.

# One way to do so is to is to: 

# pick some oil, 
# apply onto a section of chain, 
# then again pick some oil
# then apply it to the next section where oil is not applied yet
# and so on till the complete chain is oiled.

# How to use Sliding Window Technique?

# The general use of Sliding window technique can be demonstrated as following:

# Find the size of window required 
# Compute the result for 1st window, i.e. from start of data structure
# Then use a loop to slide the window by 1, and keep computing the result window by window.

# Examples to illustrate the use of Sliding window technique

# Example: Given an array of integers of size ‘n’, Our aim is to calculate the maximum sum of ‘k’ consecutive elements in the array.

# Input  : arr[] = {100, 200, 300, 400}, k = 2
# Output : 700

# Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4 
# Output : 39
# We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.

# Input  : arr[] = {2, 3}, k = 3
# Output : Invalid
# There is no subarray of size 3 as size of whole array is 2.

# code
import sys
print ("GFG")
# O(n * k) solution for finding
# maximum sum of a subarray of size k
INT_MIN = -sys.maxsize - 1

# Returns maximum sum in a
# subarray of size k.


def maxSum(arr, n, k):

	# Initialize result
	max_sum = INT_MIN

	# Consider all blocks
	# starting with i.
	for i in range(n - k + 1):
		current_sum = 0
		for j in range(k):
			current_sum = current_sum + arr[i + j]

		# Update result if required.
		max_sum = max(current_sum, max_sum)

	return max_sum


# Driver code
arr = [1, 4, 2, 10, 2,
	3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))

# This code is contributed by mits
