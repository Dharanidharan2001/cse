def max_subarr(arr,k):

    start = 0
    curr_sum = 0
    max_sum = 0

    for end , ele in enumerate(arr):
        curr_sum += ele
        if end - start + 1 == k:
            max_sum = max(max_sum,curr_sum)
            curr_sum -= arr[start]
            start += 1

    return(max_sum)

arr = [2,3,1,4,5]
#arr = list(map(int,input().split()))
k = 3

print(max_subarr(arr,k))
