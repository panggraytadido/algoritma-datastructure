# Program to display the Fibonacci sequence up to n-th term
nterms=10
# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
def find_fibonacci_seq_iter2():
   print("Fibonacci sequence:")
   while count < nterms:
      print(n1)
      nth = n1 + n2
      # update values
      n1 = n2 #swap(tukar) value
      n2 = nth #swap(tukar) value
      count += 1
    

def find_fibonacci_seq_rec(n):
   if n < 2: return n
   return find_fibonacci_seq_rec(n - 1) + find_fibonacci_seq_rec(n
   - 2)

def find_fibonacci_seq_iter(n):
   if n < 2: return n
   a, b = 0, 1
   for i in range(n):
      a, b = b, a + b
   return a

print(find_fibonacci_seq_iter(8))