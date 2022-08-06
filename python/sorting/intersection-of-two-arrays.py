nums1 = [4,9,5]
nums2 = [9,4,9,8,4]


hasil=[]
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i]==nums2[j]:
            hasil.append(nums1[i])
            break
            

# hasil = list(dict.fromkeys(hasil))
print(hasil)

