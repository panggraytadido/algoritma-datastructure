nums = [2,2,1,1,1,2,2]
nums.sort()
data =list(set(nums))

res_dict = {}
for i in range(len(data)):
    res_dict[data[i]] = 1

for i in res_dict:
    res_dict[i] = nums.count(i)

paling_sering = max(res_dict, key=res_dict.get)
