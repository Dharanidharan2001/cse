def kth_smallest(arr,k):
    arr.sort()
    return arr[k-1]
    # a = arr[::-1] to find kth largest number
    # return a[k-1]

arr=[4,3,1,5,2]
print(kth_smallest(arr,2))
