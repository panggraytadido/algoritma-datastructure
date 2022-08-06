nums1  = [1,2,2,1]
nums2= [2]

nums3=[]
for x in nums1:
    if x in nums2:
        nums2.remove(x)
        nums3.append(x)
    
print(nums3)