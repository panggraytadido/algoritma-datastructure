#O(log(n))
def merge_sort(seq):
    if len(seq) < 2 : return seq
    mid = len(seq)//2
    left, right = None, None

    if seq[:mid]: left = merge_sort([:mid])
    if seq[mid:]: right = merge_sort([mid:])

    return merge_n(left,right)

def merge_2n(left, right):
    if not left or not right:
        return left or right
    result = []

    while left and right :
        if left[-1] >= right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
            result.reversed()
    return (left or right) + result


#O(n)
def merge_n(left,right):
    if not left or not right:
        return left or right
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            result.append(left[i])
            i+=1
        else :
            result.append(right[j])
            j+=1

    if i < len(left) - 1 : result+=left[i:]
    elif j < len(right) - 1 : result += right[j:]
    return result