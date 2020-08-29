def print_arr(arr):
    # write code here
    # for x in arr:
    #     print(x),
    count = 0
    for i in range(len(arr)):
        print('index {} element {}'.format(i, arr[i]))
        if arr[i] == 2:
            count = count + 1
    return count


def set_zeroes(arr):
    # write code here
    R = len(arr)
    C = len(arr[0])

    row_set = set()
    col_set = set()

    for i in range(0, R):
        for j in range(C):
            if arr[i][j] == 0:
                row_set.add(i)
                col_set.add(j)
    print(row_set)
    print(col_set)

    for i in range(0, R):
        for j in range(C):
            if (i in row_set) or (j in col_set):
                arr[i][j] = 0



input = [2, 1, 6, 5, 4, 3, 2, 2, 2 ]
result = print_arr(input)
print('result {}'.format(result))

input = [   [2, 3, 0, 5, 0],
            [0, 4, 5, 2, 1],
            [8, 9, 3, 2, 4]]
#print(input)
set_zeroes(input)
print(input)
