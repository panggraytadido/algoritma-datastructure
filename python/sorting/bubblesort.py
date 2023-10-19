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

def bubble_sort(seq):
    size = len(seq) -1
    for num in range(size, 0, -1):
        for i in range(num):
            if seq[i] > seq[i+1]:
                temp = seq[i]
                seq[i] = seq[i+1]
                seq[i+1] = temp
    return seq

def test_bubble_sort():
    seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
    assert(bubble_sort(seq) == sorted(seq))