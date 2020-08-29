def major(arr):

    dict={}
    for element in arr:
        if element not in dict:
            dict[element] = 1
        if dict[element] > len(arr)//2:
            print(element)
        else:
            dict[element] += 1

arr=[1,2,3,2,1,2,2]
major(arr)
# nums.sort()
# print(nums[len(nums)//2])
