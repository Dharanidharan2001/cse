def plusminus(arr):
    positive_count = 0
    negative_count = 0
    zeros_count = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            positive_count += 1
        elif arr[i] < 0:
            negative_count += 1
        else:
            zeros_count += 1

    print(positive_count/len(arr))
    print(negative_count/len(arr))
    print(zeros_count/len(arr))


if __name__ == '__main__':

    #arr = list(map(int(input().rstrip().split())))
    arr = [2,1,5,-7,-4,0,-20]

    plusminus(arr)
