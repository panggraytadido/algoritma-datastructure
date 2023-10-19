nums = [1,2,3,0,0,0,1] 


opt = [item for item in set(nums) if nums.count(item) > 1]
# d =set(nums)
print(opt)

nums.remove(0)
print(nums)
# nums.sort()
# on = nums
# # cek = nums[0]
# n=nums[0]
# arr=[]
# i=0
# panjang = len(nums)-1
# for count, value in enumerate(nums):
#     if count<panjang and nums[count]==nums[count+1]:
#         nums.remove(nums[count])

# for elem in nums:
#     if i < panjang:
#         if nums[i]==nums[i+1]:
#             print()
        # if nums[i]==n and nums[i+1]==n:
        #     print('')
        #     # nums.remove(elem)
        #     # print('')
        #     # del nums[i]
        # if nums[i]==n and nums[i+1]!=n:
        #     n=nums[i+1]

    # if elem==cek:
    #     print(n)
    # else:
    #     n=elem
    #     arr.append(elem)
    # i=i+1

# print(n)
# print(nums)
# list(filter(lambda a: a != 0, nums1))
# list(filter((0).__ne__, nums1))
# nums1[:] = (value for value in nums1 if value != 0)
# print(nums1)
# print(arr)
# nums1.remove(0)
# print(nums1)
# for i in range(len(nums1)):
    # print(nums1[i])
    # if nums1[i]==cek:
        # del nums1[0]
        # nums1.pop(i)
    # if i<len(nums1)-1:
    #     if nums1[i]==nums1[i+1]:
    #         cek.add(nums1[i])
    
# print(len(nums1))
# mylist = list(dict.fromkeys(nums1))
# print(nums1)
